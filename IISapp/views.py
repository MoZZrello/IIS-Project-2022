from django.http import HttpRequest
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

import datetime

from .decorators import *
from .forms import *
from .filters import *
from .models import *


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


def about(request: HttpRequest) -> HttpResponse:
    animals = Animal.objects.all()

    animalFilter = AnimalFilter(request.GET, queryset=animals)
    animals = animalFilter.qs

    context = {'animals': animals, 'myFilter': animalFilter}
    return render(request, 'about.html', context)


def animal_profile(request, animalid):
    user = request.user
    animal = Animal.objects.get(id=animalid)

    record = Record.objects.filter(animal=animal).exclude(record_type="Zdravotní záznam")
    healt_records = Record.objects.filter(animal=animal, record_type="Zdravotní záznam")

    record_count = record.count()
    health_record_count = healt_records.count()

    context = {'animal': animal, 'user': user, 'healt_records': healt_records, 'record': record,
               'record_count': record_count, 'health_record_count': health_record_count}
    return render(request, 'animal_page.html', context)


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
    walks_active = outing_reservation.objects.filter(user_name=request.user.id,
                                                     outing_start__gte=datetime.datetime.now())

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


@login_required(login_url='login')
@allowed_users(allowed_roles=['Pečovatel'])
def walks_dashboard(request):
    user = request.user
    reservations = outing_reservation.objects.all()
    requests = Requests.objects.filter(request_name="Venčení", veterinary_req=False, request_verification=False)
    record_count = requests.count()

    not_vets = User.objects.exclude(role=3)
    vet_requests = outing_reservation.objects.filter(user_name__isnull=False, outing_start__gte=datetime.datetime.now())
    for people in not_vets:
        vet_requests = vet_requests.exclude(user_name=people)
    vet_count = vet_requests.count()

    outingFilter = OutingsFilter(request.GET, queryset=reservations)
    reservations = outingFilter.qs

    context = {'user': user,
               'reservations': reservations,
               'requests': requests,
               'outingFilter': outingFilter,
               'record_count': record_count,
               'vet_requests': vet_requests,
               'vet_count': vet_count}
    return render(request, 'walks_dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Pečovatel'])
def verify_request(request, reqid, resid):
    outing_reservation.objects.filter(id=resid).update(outing_verification=True)
    Requests.objects.filter(id=reqid).update(request_verification=True)
    return redirect('walks_dashboard')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Dobrovolník'])
def reservation(request):
    user = request.user
    not_assigned_reservations = outing_reservation.objects.filter(user_name__isnull=True,
                                                                  outing_start__gte=datetime.datetime.now())
    assigned_reservations = outing_reservation.objects.filter(user_name=user.id,
                                                              outing_start__gte=datetime.datetime.now())

    context = {'user': user, 'not_assigned_reservations': not_assigned_reservations,
               'assigned_reservations': assigned_reservations}
    return render(request, 'walks_reservations.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Dobrovolník'])
def assign_walk(request, resid, name):
    outing_reservation.objects.filter(id=resid).update(user_name=name, outing_verification=False)
    outing = outing_reservation.objects.get(id=resid)
    r = Requests(contractor=outing.user_name,
                 animal=outing.animal,
                 datetime_start=outing.outing_start,
                 datetime_end=outing.outing_end,
                 veterinary_req=False,
                 request_name="Venčení",
                 request_verification=False,
                 outing_assigned=outing,
                 )
    r.save()
    return redirect('reservation')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Dobrovolník'])
def unassign_walk(request, resid):
    outing = outing_reservation.objects.filter(id=resid).update(user_name=None, outing_verification=False)
    r = Requests.objects.filter(outing_assigned=outing)
    if r is not None:
        r.delete()
    return redirect('reservation')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Pečovatel', 'Veterinář'])
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
@allowed_users(allowed_roles=['Pečovatel'])
def volunteer_verification(request):
    unverified_volunteers = User.objects.filter(role=4, user_verification=False)
    verified_volunteers = User.objects.filter(role=4, user_verification=True)

    unverify_counter = unverified_volunteers.count()
    verify_counter = verified_volunteers.count()

    context = {'verify_counter': verify_counter, 'unverify_counter': unverify_counter,
               'unverified_volunteers': unverified_volunteers, 'verified_volunteers': verified_volunteers}
    return render(request, 'volunteer_verification.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Pečovatel'])
def verify_volunteer(request, userid):
    User.objects.filter(id=userid).update(user_verification=1)
    return redirect('volunteer_verification')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Pečovatel'])
def unverify_volunteer(request, userid):
    User.objects.filter(id=userid).update(user_verification=0)
    return redirect('volunteer_verification')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Veterinář'])
def all_vet_requests(request):
    user = request.user
    requests = Requests.objects.filter(veterinary_req=True)
    next_requests = Requests.objects.filter(veterinary_req=True, solver=user,
                                            datetime_start__gte=datetime.datetime.now())
    context = {'user': user, 'requests': requests, 'next_requests': next_requests}
    return render(request, 'all_vet_requests.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Pečovatel'])
def add_vet_request(request):
    form = CreateVetRequestForm()

    if request.method == 'POST':
        form = CreateVetRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_animals')

    context = {'form': form}
    return render(request, 'add_vet_request.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Veterinář'])
def vet_request_edit(request, pk):
    vet_request = Requests.objects.filter(id=pk).first()
    form2 = EditVetRequest(instance=vet_request)

    if request.method == 'POST':
        form2 = EditVetRequest(request.POST, request.FILES, instance=vet_request)
        if form2.is_valid():
            form2.save()

    context = {'form2': form2}
    return render(request, 'vet_request_edit.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Veterinář'])
def make_reservation(request, reqid):
    Requests.objects.filter(id=reqid).update(request_verification=False)
    req = Requests.objects.get(id=reqid)
    reserve = outing_reservation(user_name=req.solver,
                                 animal=req.animal,
                                 outing_start=req.datetime_start,
                                 outing_end=req.datetime_end,
                                 outing_verification=True,
                                 outing_assigned=True)
    reserve.save()
    return redirect('all_vet_requests')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Administrátor'])
def admin_site(request):
    users = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=users)
    users = user_filter.qs
    context = {'users': users, 'user_filter': user_filter}

    return render(request, 'admin_site.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Administrátor'])
def user_desc(request, userid):
    user2 = User.objects.get(id=userid)
    context = {'user2': user2}
    return render(request, 'user_desc.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Administrátor'])
def user_delete(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('admin_site')

    context = {'user': user}
    return render(request, 'user_delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Administrátor'])
def user_to_veterinary(request, pk):
    User.objects.filter(id=pk).update(role=3)
    return redirect('admin_site')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Administrátor'])
def user_to_keeper(request, pk):
    User.objects.filter(id=pk).update(role=2)
    return redirect('admin_site')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Administrátor'])
def user_to_admin(request, pk):
    User.objects.filter(id=pk).update(role=1)
    return redirect('admin_site')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Administrátor'])
def user_verification(request, pk):
    User.objects.filter(id=pk).update(user_verification=True)
    return redirect('admin_site')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Administrátor'])
def user_update(request, pk):
    user = User.objects.filter(id=pk).first()
    form = ProfileForm(instance=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'user_update.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Pečovatel'])
def add_record(request, pk):
    form = AddRecordForm({'animal': pk})

    if request.method == 'POST':
        form = AddRecordForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('all_animals')

    context = {'form': form}
    return render(request, 'add_record.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Veterinář'])
def add_health_record(request, pk):
    form = AddRecordForm({'animal': pk, 'record_type': "Zdravotní záznam"})

    if request.method == 'POST':
        form = AddRecordForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('all_animals')

    context = {'form': form}
    return render(request, 'add_record.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Veterinář', 'Pečovatel'])
def edit_record(request, pk):
    rec = Record.objects.filter(id=pk).first()
    form2 = AddRecordForm(instance=rec)

    if request.method == 'POST':
        form2 = AddRecordForm(request.POST, request.FILES, instance=rec)
        if form2.is_valid():
            form2.save()
            return redirect('/animal/all/' + str(rec.animal.id) + '/')

    context = {'form2': form2}
    return render(request, 'edit_record.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Veterinář', 'Pečovatel'])
def delete_record(request, pk):
    rec = Record.objects.get(id=pk)
    if request.method == 'POST':
        rec.delete()
        return redirect('/animal/all/' + str(rec.animal.id) + '/')

    context = {'rec': rec}
    return render(request, 'delete_record.html', context)
