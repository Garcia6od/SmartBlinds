from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from login.models import Usuario, Alarma


def login1(request):
    return render(request, 'login/index.html')


@login_required()
def controls(request):
    return render(request, 'login/controls.html')


def alarma(request):
    return render(request, 'login/alarma.html')


def login_user(request):
    if request.method == 'POST':
        nombre = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=nombre, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return redirect('login1')
    else:
        return redirect('login1')


def register(request):
    return render(request, 'login/register.html')


def register_user(request):
    if request.method == 'POST':
        nombre = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = Usuario.objects.create_user(nombre, email, password)
        user.save()
        return render(request, 'login/index.html')


def logout_user(request):
    logout(request)
    return render(request, 'login/index.html')


@login_required()
def profile(request):
    return render(request, 'login/base.html')


def guest(request):
    request.session['guest'] = True
    return redirect('controls')


def alarma_user(request):
    if request.method == 'POST':
        open = request.POST['hora_open']
        close = request.POST['hora_close']

        alarma = Alarma()
        alarma.usuario = request.user
        alarma.hora_open = open
        alarma.hora_close = close
        alarma.save()

        alarmas = Alarma.objects.all()

    context = {'alarmas': alarmas}
    return render(request, 'login/alarma.html',context)
