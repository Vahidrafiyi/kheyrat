# Generated by Django 4.0.3 on 2022-04-04 10:01

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_prayer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fast',
            name='user',
            field=phone_field.models.PhoneField(blank=True, help_text='to send sms when charity done...', max_length=31),
        ),
        migrations.AlterField(
            model_name='quran',
            name='user',
            field=phone_field.models.PhoneField(blank=True, help_text='to send sms when charity done...', max_length=31),
        ),
    ]