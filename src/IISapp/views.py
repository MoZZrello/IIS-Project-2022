from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import datetime

from .decorators import *
from .forms import *
from .models import *
from .filters import *


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


def about(request: HttpRequest) -> HttpResponse:
    animals = Animal.objects.all()

    animalFilter = AnimalFilter(request.GET, queryset=animals)
    animals = animalFilter.qs

    context = {'animals': animals, 'myFilter': animalFilter}
    return render(request, 'about.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Dobrovolník', 'Veterinář', 'Pečovatel'])
def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')


@unauthenticated_user
def login_page(request):
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


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('index')


@unauthenticated_user
def register_page(request):
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['Dobrovolník', 'Veterinář', 'Pečovatel'])
def user_profile(request):
    user = request.user
    form = ProfileForm(instance=user)

    walks = outing_reservation.objects.filter(user_name=request.user.id)
    walks_active = outing_reservation.objects.filter(user_name=request.user.id, outing_start__gte=datetime.datetime.now())

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

    context = {'walks': walks, 'walks_active': walks_active, 'form': form}
    return render(request, 'profil.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Pečovatel'])
def create_walk(request):
    form = CreateWalkForm()

    if request.method == 'POST':
        form = CreateWalkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('walks_dashboard')

    context = {'form': form}
    return render(request, 'walk_creator.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Pečovatel'])
def update_walk(request, pk):
    reservation = outing_reservation.objects.get(id=pk)
    form = CreateWalkForm(instance=reservation)

    if request.method == 'POST':
        form = CreateWalkForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('walks_dashboard')

    context = {'form': form}
    return render(request, 'walk_creator.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Pečovatel'])
def delete_walk(request, pk):
    walk = outing_reservation.objects.get(id=pk)

    if request.method == 'POST':
        walk.delete()
        return redirect('walks_dashboard')

    context = {'walk': walk}
    return render(request, 'walk_delete.html', context)


@allowed_users(allowed_roles=['Pečovatel'])
def walks_dashboard(request):
    reservations = outing_reservation.objects.all()
    context = {'reservations': reservations}
    return render(request, 'walks_dashboard.html', context)
