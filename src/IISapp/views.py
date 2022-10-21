from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

import datetime
from calendar import HTMLCalendar

from .decorators import *
from .forms import *
from .filters import *
from .random_functions import *


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

    walks = outing_reservation.objects.filter(user_name=request.user.id, outing_start__lt=datetime.datetime.now())
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
    user = request.user
    reservations = outing_reservation.objects.all()
    context = {'user': user, 'reservations': reservations}
    return render(request, 'walks_dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Dobrovolník'])
def assign_walk(request, resid, name):
    outing_reservation.objects.filter(id=resid).update(user_name=name, outing_verification=False)
    return redirect('reservation')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Dobrovolník'])
def unassign_walk(request, resid):
    outing_reservation.objects.filter(id=resid).update(user_name=None, outing_verification=False)
    return redirect('reservation')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Dobrovolník'])
def reservation(request):
    user = request.user
    not_assigned_reservations = outing_reservation.objects.filter(user_name__isnull=True, outing_start__gte=datetime.datetime.now())
    assigned_reservations = outing_reservation.objects.filter(user_name=user.id, outing_start__gte=datetime.datetime.now())

    context = {'user': user, 'not_assigned_reservations': not_assigned_reservations, 'assigned_reservations': assigned_reservations}
    return render(request, 'walks_reservations.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Pečovatel'])
def all_animals(request):
    user = request.user
    animals = Animal.objects.all()
    context = {'user': user, 'animals': animals}
    return render(request, 'animal_all.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Pečovatel'])
def add_animals(request):
    form = CreateAnimalForm()

    if request.method == 'POST':
        form = CreateAnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_animals')

    context = {'form': form}
    return render(request, 'animal_add.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Pečovatel'])
def update_animals(request, pk):
    animal = Animal.objects.get(id=pk)
    form = CreateAnimalForm(instance=animal)

    if request.method == 'POST':
        form = CreateAnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('all_animals')

    context = {'form': form}
    return render(request, 'animal_add.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Pečovatel'])
def delete_animals(request, pk):
    animal = Animal.objects.get(id=pk)
    if request.method == 'POST':
        animal.delete()
        return redirect('all_animals')

    context = {'animal': animal}
    return render(request, 'animal_delete.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Administrátor'])
def admin_site(request):
    users = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=users)
    users = user_filter.qs
    context = {'users': users, 'user_filter': user_filter}
    return render(request, 'admin_site.html', context)
