# Generated by Django 4.1.2 on 2022-11-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IISapp', '0018_alter_requests_request_verification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
