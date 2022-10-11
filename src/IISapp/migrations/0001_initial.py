# Generated by Django 3.2.12 on 2022-10-11 19:11

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_name', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=255)),
                ('breed', models.CharField(blank=True, max_length=255)),
                ('age', models.SmallIntegerField()),
                ('animal_description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='')),
                ('capture_date', models.DateField()),
                ('outing_suitable', models.BooleanField()),
                ('animal_verification', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User_roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Administrátor'), (2, 'Pečovatel'), (3, 'Veterinář'), (4, 'Dobrovolník'), (5, 'Neregistrovaný uživatel')], default=5)),
                ('user_manage', models.BooleanField()),
                ('animal_manage', models.BooleanField()),
                ('schedule_manage', models.BooleanField()),
                ('verify_volunteers', models.BooleanField()),
                ('verify_reservations', models.BooleanField()),
                ('make_requests', models.BooleanField()),
                ('make_veterinary_requests', models.BooleanField()),
                ('handle_requests', models.BooleanField()),
                ('handle_veterinary_requests', models.BooleanField()),
                ('edit_reports', models.BooleanField()),
                ('edit_veterinary_reports', models.BooleanField()),
                ('make_reservations', models.BooleanField()),
                ('outing_history_view', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('birthdate', models.DateField()),
                ('phone_numb', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=255, region=None)),
                ('mail', models.EmailField(blank=True, max_length=255)),
                ('user_verification', models.BooleanField()),
                ('user_name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IISapp.user_roles')),
            ],
        ),
        migrations.CreateModel(
            name='requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_start', models.DateTimeField()),
                ('datetime_end', models.DateTimeField(blank=True)),
                ('veterinary_req', models.BooleanField()),
                ('request_name', models.CharField(max_length=255)),
                ('request_description', models.TextField(blank=True)),
                ('request_verification', models.BooleanField()),
                ('animal', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='IISapp.animal')),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractor_name', to='IISapp.user')),
                ('solver', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='solver_name', to='IISapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_name', models.CharField(max_length=255)),
                ('record_type', models.CharField(max_length=255)),
                ('record_description', models.TextField(blank=True)),
                ('record_start', models.DateTimeField()),
                ('record_end', models.DateTimeField(blank=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IISapp.animal')),
            ],
        ),
        migrations.CreateModel(
            name='outing_reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outing_start', models.DateTimeField()),
                ('outing_end', models.DateTimeField(blank=True)),
                ('outing_verification', models.BooleanField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IISapp.animal')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IISapp.user')),
            ],
        ),
    ]
