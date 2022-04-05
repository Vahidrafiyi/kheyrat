# Generated by Django 4.0.3 on 2022-04-04 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_fast_done_prayer_done_quran_done_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prayer',
            old_name='prayer_type',
            new_name='type',
        ),
        migrations.AddField(
            model_name='fast',
            name='type',
            field=models.CharField(choices=[('روزه واجب', 'روزه واجب'), ('روزه مستحبی', 'روزه مستحبی')], default='روزه واجب', max_length=24),
        ),
    ]