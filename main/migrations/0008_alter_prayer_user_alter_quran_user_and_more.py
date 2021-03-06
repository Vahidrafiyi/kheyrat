# Generated by Django 4.0.3 on 2022-04-05 08:14

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_salavat_alter_fast_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prayer',
            name='user',
            field=phone_field.models.PhoneField(blank=True, help_text='to send sms when charity done...', max_length=31, null=True),
        ),
        migrations.AlterField(
            model_name='quran',
            name='user',
            field=phone_field.models.PhoneField(blank=True, help_text='to send sms when charity done...', max_length=31, null=True),
        ),
        migrations.AlterField(
            model_name='salavat',
            name='user',
            field=phone_field.models.PhoneField(blank=True, help_text='to send sms when charity done...', max_length=31, null=True),
        ),
    ]
