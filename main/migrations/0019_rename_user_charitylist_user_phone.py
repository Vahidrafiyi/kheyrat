# Generated by Django 4.0.3 on 2022-04-19 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_charitylist_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='charitylist',
            old_name='user',
            new_name='user_phone',
        ),
    ]