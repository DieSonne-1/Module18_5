from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.

users = ['Tony', 'Jack', 'Mia']


def sign_up_by_html(request):
    info = {}
    context = {
        'info': info,
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return HttpResponse(f'Пароли не совпадают', status=400, reason='incorrect rassword')
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return HttpResponse(f'Вы должны быть старше 18', status=400, reason='incorrect age')
        if username in users:
            info['error'] = 'Пользователь уже существует'
            return HttpResponse(f'Пользователь уже существует', status=400, reason='incorrect login')
        else:
            return HttpResponse(f'Приветствуем, {username}!')
    return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return HttpResponse(f'Пароли не совпадают', status=400, reason='incorrect rassword')
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return HttpResponse(f'Вы должны быть старше 18', status=400, reason='incorrect age')
            if username in users:
                info['error'] = 'Пользователь уже существует'
                return HttpResponse(f'Пользователь уже существует', status=400, reason='incorrect login')
            else:
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
        context = {
            'info': info,
            'form': form
        }
        return render(request, 'fifth_task/registration_page.html', context)
