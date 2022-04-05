# Generated by Django 4.0.3 on 2022-04-05 05:28

from django.db import migrations, models
import django_jalali.db.models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_fast_user_alter_quran_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salavat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', phone_field.models.PhoneField(blank=True, help_text='to send sms when charity done...', max_length=31)),
                ('how_many', models.PositiveSmallIntegerField()),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='fast',
            name='user',
            field=phone_field.models.PhoneField(blank=True, help_text='to send sms when charity done...', max_length=31, null=True),
        ),
    ]