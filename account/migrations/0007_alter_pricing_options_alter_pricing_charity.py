# Generated by Django 4.0.3 on 2022-04-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_pricing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricing',
            options={'verbose_name': 'pricing', 'verbose_name_plural': 'pricing'},
        ),
        migrations.AlterField(
            model_name='pricing',
            name='charity',
            field=models.CharField(choices=[('یک روز کامل', 'یک روز کامل'), ('ختم', 'ختم'), ('جزء', 'جزء'), ('صلوات', 'صلوات'), ('روزه', 'روزه'), ('نماز آیات', 'نماز آیات'), ('نماز نذر', 'نماز نذر'), ('نماز احتیاط', 'نماز احتیاط'), ('نماز میت', 'نماز میت'), ('نماز نافله', 'نماز نافله'), ('نماز جعفر طیار', 'نماز جعفر طیار'), ('نماز لیله الدفن', 'نماز لیله الدفن'), ('نماز شب', 'نماز شب')], max_length=24),
        ),
    ]
