# Generated by Django 4.0.3 on 2022-04-07 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_fast_alter_profile_prayer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
