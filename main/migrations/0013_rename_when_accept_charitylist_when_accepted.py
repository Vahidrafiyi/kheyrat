# Generated by Django 4.0.3 on 2022-04-08 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_delete_fast_delete_prayer_delete_quran_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='charitylist',
            old_name='when_accept',
            new_name='when_accepted',
        ),
    ]