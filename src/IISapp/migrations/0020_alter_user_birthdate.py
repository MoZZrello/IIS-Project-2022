# Generated by Django 4.1.2 on 2022-11-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IISapp', '0019_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(blank=True),
        ),
    ]
