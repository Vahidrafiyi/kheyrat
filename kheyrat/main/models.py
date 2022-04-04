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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=24, choices=PRAYER_TYPE, default=PRAYER_TYPE[2][1])
    what_kind = models.CharField(max_length=32, choices=WHAT_KIND, blank=True, null=True)
    how_many = models.PositiveSmallIntegerField()
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Fast(models.Model):
    TYPE = (
        ('روزه واجب', 'روزه واجب'),
        ('روزه مستحبی', 'روزه مستحبی'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=24, choices=TYPE, default=TYPE[0][1])
    how_many = models.PositiveSmallIntegerField()
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Quran(models.Model):
    TYPE = (
        ('ختم', 'ختم'),
        ('جزء', 'جزء'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=12, choices=TYPE, default=TYPE[1][1])
    how_many = models.PositiveSmallIntegerField()
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


