from django.db import models
from django.db.models import PROTECT, SET_DEFAULT, CASCADE
from phonenumber_field.modelfields import PhoneNumberField


class User_roles(models.Model):
    # role v systemu
    ADMIN = 1
    KEEPER = 2
    VETERINARY = 3
    VOLUNTEER = 4

    ROLES = (
        (ADMIN, 'Administrátor'),
        (KEEPER, 'Pečovatel'),
        (VETERINARY, 'Veterinář'),
        (VOLUNTEER, 'Dobrovolník'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLES, default=VOLUNTEER)
    user_manage = models.BooleanField()
    animal_manage = models.BooleanField()
    schedule_manage = models.BooleanField()
    verify_volunteers = models.BooleanField()
    verify_reservations = models.BooleanField()
    make_requests = models.BooleanField()
    make_veterinary_requests = models.BooleanField()
    handle_requests = models.BooleanField()
    handle_veterinary_requests = models.BooleanField()
    edit_reports = models.BooleanField()
    edit_veterinary_reports = models.BooleanField()
    make_reservations = models.BooleanField()
    outing_history_view = models.BooleanField()

    def __str__(self):
        return self.role


class User(models.Model):
    role = models.ForeignKey(User_roles, on_delete=CASCADE)
    full_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    phone_numb = PhoneNumberField(max_length=255, blank=True)
    mail = models.EmailField(max_length=255, blank=True)
    user_verification = models.BooleanField()
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name


class Animal(models.Model):
    animal_name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255, blank=True)
    age = models.SmallIntegerField()
    animal_description = models.TextField(blank=True)
    image = models.ImageField()
    capture_date = models.DateField()
    outing_suitable = models.BooleanField()
    animal_verification = models.BooleanField()


class outing_reservation(models.Model):
    user_name = models.ForeignKey(User, on_delete=CASCADE)
    animal = models.ForeignKey(Animal, on_delete=CASCADE)
    outing_start = models.DateTimeField()
    outing_end = models.DateTimeField(blank=True)
    outing_verification = models.BooleanField()


class record(models.Model):
    animal = models.ForeignKey(Animal, on_delete=CASCADE)
    record_name = models.CharField(max_length=255)
    record_type = models.CharField(max_length=255)
    record_description = models.TextField(blank=True)


class requests(models.Model):
    contractor = models.ForeignKey(User, on_delete=CASCADE, related_name='contractor_name')
    solver = models.ForeignKey(User, on_delete=PROTECT, blank=True, related_name='solver_name')
    animal = models.ForeignKey(Animal, on_delete=CASCADE, blank=True)
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField(blank=True)
    veterinary_req = models.BooleanField()
    request_name = models.CharField(max_length=255)
    request_description = models.TextField(blank=True)
    request_verification = models.BooleanField()
