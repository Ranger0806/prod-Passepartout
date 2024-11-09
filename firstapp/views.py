from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import ProjectUserRegisterForm


# Create your views here.
def main(request):
    return render(request, template_name='first_page.html')


def authentication(request):
    context = {
        'auth': request.user.is_authenticated
    }
    return render(request, template_name='auth.html', context=context)


def register(request):
    context = {
        'auth': request.user.is_authenticated
    }
    return render(request, template_name='register.html', context=context)


def register_process(request):
    if request.method == 'POST':
        try:
            form = ProjectUserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.save()
            else:
                context = {
                    'error': form.errors
                }
                return render(request, template_name='register.html', context=context)
            return redirect('firstapp:authenticate')
        except Exception as e:
            print(e)
            context = {
                'auth': request.user.is_authenticated,
                'error': 'Ошибка регистрации, попробуйте снова.'
            }
            return render(request, template_name='register.html', context=context)


def authorization(request):
    return None


def authentication_process(request):
    if request.method == 'POST':
        login_user = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=login_user, password=password)
        if user:
            login(request, user)
            print("I love Muslim")
