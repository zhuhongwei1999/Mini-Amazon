# Generated by Django 4.1.5 on 2023-04-27 16:18

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/wall.jpg', null=True, upload_to=users.models.profile_image_path),
        ),
    ]
