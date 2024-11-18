# Generated by Django 2.2.24 on 2024-11-15 03:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20241113_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaints',
            old_name='address_complaints',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='complaints',
            old_name='text_complaints',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]