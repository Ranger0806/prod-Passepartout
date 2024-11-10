from io import BytesIO
from django.http import FileResponse
from django.shortcuts import render, redirect
from mainapp.models import Tickets
from django.contrib.auth.decorators import login_required
from datetime import date, datetime


@login_required
def main(request):
    try:
        context = {
            'content': []
        }
        for content in Tickets.objects.filter(user_id=request.user.id).order_by('date_start'):
            context['content'].append(
                {'date': content.date_start, 'ticket': '',
                'country': content.country, 'id': content.id, 'price': content.price})
        return render(request, 'main.html', context=context)
    except Exception as e:
        context = {
            'error': "Something went wrong."
        }
        return render(request, 'main.html', context=context)


@login_required
def add_trip(request):
    return render(request, 'add_trip.html')

@login_required
def process_add_trip(request):
    if request.method == 'POST':
        try:
            country = request.POST['country']
            date_trip = request.POST['date_start']
            date_end_trip = request.POST['date_end']
            price = request.POST['price']
            trip_plan = request.POST['trip_plan']
            file_upload = request.FILES['file']
            if datetime.strptime(date_trip, "%Y-%m-%d").date() < date.today():
                return render(request, 'add_trip.html', context={'error': "Дата должна быть не раньше текущей!"})
            if country and date and file_upload and price:
                file_read = file_upload.read()
                trip = Tickets.objects.create(user_id=request.user.id, country=country, date_start=date_trip, date_end=date_end_trip, ticket=file_read, price=price, trip_plan=trip_plan)
                trip.save()
                return redirect('mainapp:main')
            return render(request, 'add_trip.html', context={'error': 'Не все поля заполнены!'})
        except Exception as e:
            print(e)
            context = {
                'error': "Something went wrong."
            }
            return render(request, 'add_trip.html', context=context)

@login_required
def download(request, id):
    file = Tickets.objects.get(id=id).ticket
    io_file = BytesIO(file)
    response = FileResponse(io_file, content_type='application/pdf', filename='ticket.pdf')
    return response

@login_required
def statistics(request):
    user_data = Tickets.objects.filter(user_id=request.user.id, date_start__lt=date.today())
    count_country = user_data.values("country").distinct().count()
    user_data = Tickets.objects.filter(user_id=request.user.id, date_start__month=date.today().month, date_start__year=date.today().year)
    sum_price_month = 0
    for i in user_data.values('price'):
        sum_price_month += int(i['price'][:-1])
    user_data = Tickets.objects.filter(user_id=request.user.id, date_start__gte=date.today())
    trips_count = user_data.count()
    context = {'count_country': count_country, 'sum_price_month': sum_price_month, 'later_trips': [], 'trips_count': trips_count if trips_count > 0 else 'Нет предстоящих поездок'}
    for content in user_data:
        context['later_trips'].append({'trip_to': content.country, 'trip_late': (content.date_end - content.date_start).days, 'trip_plan': content.trip_plan})
    return render(request, 'statistics.html', context=context)
