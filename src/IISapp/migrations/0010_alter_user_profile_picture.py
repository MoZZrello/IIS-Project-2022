# Generated by Django 4.1.1 on 2022-10-20 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IISapp', '0009_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pic_default.jpg', null=True, upload_to='static/img'),
        ),
    ]
