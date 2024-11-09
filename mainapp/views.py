from django.shortcuts import render, redirect
from mainapp.models import Tickets
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    try:
        context = {
            'content': []
        }
        for content in Tickets.objects.filter(user_id=request.user.id):
            context['content'].append({'date': content.date, 'ticket': content.ticket, 'country': content.country})
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
            print(request.FILES)
            country = request.POST['country']
            date = request.POST['date']
            file_upload = request.FILES['file']
            if country and date and file_upload:
                file_data = file_upload.read()
                trip = Tickets.objects.create(user_id=request.user.id, country=country, date=date, ticket=file_data)
                trip.save()
                return redirect('mainapp:main')
            return render(request, 'add_trip.html', context={'error': 'Не все поля заполнены!'})
        except Exception as e:
            print(e)
            context = {
                'error': "Something went wrong."
            }
            return render(request, 'add_trip.html', context=context)