# Generated by Django 4.0.3 on 2022-04-11 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_profile_first_name_remove_profile_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fast',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='prayer',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='quran',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='salavat',
        ),
    ]
