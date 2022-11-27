# Generated by Django 4.1.1 on 2022-10-21 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IISapp', '0012_alter_outing_reservation_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outing_reservation',
            name='user_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]