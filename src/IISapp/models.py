from django.db import models
from django.db.models import PROTECT, SET_DEFAULT, CASCADE
from django.contrib.auth.models import AbstractUser


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
        return f'{self.role}'


class User(AbstractUser):
    role = models.ForeignKey(User_roles, on_delete=CASCADE, default=4)
    full_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    phone_number = models.CharField(max_length=255, blank=True)
    mail = models.EmailField(max_length=255, blank=True)
    user_verification = models.BooleanField(default=0)
    user_name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='static/img', blank=True, null=True)

    username = None
    USERNAME_FIELD = 'user_name'

    def __str__(self):
        return self.user_name

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Animal(models.Model):
    animal_name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255, blank=True)
    age = models.SmallIntegerField()
    animal_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='static/img', blank=True, null=True)
    capture_date = models.DateField()
    outing_suitable = models.BooleanField()
    animal_verification = models.BooleanField()


class outing_reservation(models.Model):
    user_name = models.ForeignKey(User, on_delete=CASCADE, blank=True, null=True)
    animal = models.ForeignKey(Animal, on_delete=CASCADE)
    outing_start = models.DateTimeField()
    outing_end = models.DateTimeField(blank=True)
    outing_verification = models.BooleanField()
    outing_assigned = models.BooleanField(default=False)


class Record(models.Model):
    animal = models.ForeignKey(Animal, on_delete=CASCADE)
    record_name = models.CharField(max_length=255)
    record_type = models.CharField(max_length=255)
    record_description = models.TextField(blank=True)


class Requests(models.Model):
    contractor = models.ForeignKey(User, on_delete=CASCADE, related_name='contractor_name')
    solver = models.ForeignKey(User, on_delete=PROTECT, blank=True, null=True, related_name='solver_name')
    animal = models.ForeignKey(Animal, on_delete=CASCADE, blank=True)
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField(blank=True)
    veterinary_req = models.BooleanField()
    request_name = models.CharField(max_length=255)
    request_description = models.TextField(blank=True)
    request_verification = models.BooleanField(default=False)
    outing_assigned = models.ForeignKey(outing_reservation, on_delete=CASCADE, blank=True, null=True)
