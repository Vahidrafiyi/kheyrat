from django.contrib.auth.models import User
from django.db import models
from django_jalali.db import models as jmodels
class Prayer(models.Model):
    PRAYER_TYPE = (
        ('نماز واجب', 'نماز واجب'),
        ('نماز مستحب', 'نماز مستحب'),
        ('یک روز کامل', 'یک روز کامل'),
    )
    WHAT_KIND = (
        # نماز های واجب
        ('نماز آیات', 'نماز آیات'),
        ('نماز نذر', 'نماز نذر'),
        ('نماز احتیاط', 'نماز احتیاط'),
        ('نماز میت', 'نماز میت'),
        # نماز های مستحب
        ('نماز نافله', 'نماز نافله'),
        ('نماز جعفر طیار', 'نماز جعفر طیار'),
        ('نماز لیله الدفن', 'نماز لیله الدفن'),
        ('نماز شب', 'نماز شب'),
    )
    user = models.ManyToManyField(User)
    prayer_type = models.CharField(max_length=24, choices=PRAYER_TYPE, default=PRAYER_TYPE[2][1])
    what_kind = models.CharField(max_length=32, choices=WHAT_KIND, blank=True, null=True)
    how_many = models.PositiveSmallIntegerField()
    created_at = jmodels.jDateTimeField()

class Fast(models.Model):
    user = models.ManyToManyField(User)
    how_many = models.PositiveSmallIntegerField()
    created_at = jmodels.jDateTimeField()


class Quran(models.Model):
    TYPE = (
        ('ختم', 'ختم'),
        ('جزء', 'جزء'),
    )
    user = models.ManyToManyField(User)
    type = models.CharField(max_length=12, choices=TYPE, default=TYPE[1][1])
    how_many = models.PositiveSmallIntegerField()
    created_at = jmodels.jDateTimeField()


