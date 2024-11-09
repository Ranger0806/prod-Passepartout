from lib2to3.fixes.fix_input import context

from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, template_name='first_page.html')


def authentication(request):
    if request.method == 'POST':
        context = {
            'auth': request.user.is_authenticated
        }
        return render(request, template_name='auth.html', context=context)


def register(request):
    return render(request, template_name='register.html')


def register_process(request):
    return None


def authorization(request):
    return None


def authentication_process(request):
    return None