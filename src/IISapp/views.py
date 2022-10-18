from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


@login_required(login_url='login')
def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        context = {}
        if request.method == 'POST':
            username = request.POST.get('user_name')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Přezívka nebo heslo nejsou správné')
                return render(request, 'login.html', context)

        return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('user_name')
                messages.success(request, 'Účet uspešne vytvořen pro: ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)


def user_profil(request):
    return render(request, 'profil.html')
