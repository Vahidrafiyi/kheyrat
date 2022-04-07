from django.contrib.auth.models import User
from django.db import models

from phone_field import PhoneField
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
    user = PhoneField(blank=True, null=True, help_text='to send sms when charity done...')
    type = models.CharField(max_length=24, choices=PRAYER_TYPE, default=PRAYER_TYPE[2][1])
    what_kind = models.CharField(max_length=32, choices=WHAT_KIND, blank=True, null=True)
    how_many = models.PositiveSmallIntegerField()
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if self.user is not None:
            self.user = ('+98') + str(self.user)
        super().save(*args, **kwargs)

class Fast(models.Model):
    user = PhoneField(blank=True, null=True, help_text='to send sms when charity done...')
    how_many = models.PositiveSmallIntegerField()
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if self.user is not None:
            self.user = ('+98') + str(self.user)
        super().save(*args, **kwargs)

class Quran(models.Model):
    TYPE = (
        ('ختم', 'ختم'),
        ('جزء', 'جزء'),
    )
    user = PhoneField(blank=True, null=True, help_text='to send sms when charity done...')
    type = models.CharField(max_length=12, choices=TYPE, default=TYPE[1][1])
    how_many = models.PositiveSmallIntegerField()
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if self.user is not None:
            self.user = ('+98') + str(self.user)
        super().save(*args, **kwargs)

class Salavat(models.Model):
    user = PhoneField(blank=True, null=True, help_text='to send sms when charity done...')
    how_many = models.PositiveSmallIntegerField()
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if self.user is not None:
            self.user = ('+98') + str(self.user)
        super().save(*args, **kwargs)


class CharityList(models.Model):
    charity_type = models.CharField(max_length=16)
    quantity = models.PositiveSmallIntegerField()
    accepted = models.BooleanField(default=False)
    created_at = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return self.charity_type





