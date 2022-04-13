import random

from django.contrib.auth.models import User
from django.db import models

from phone_field import PhoneField
from django_jalali.db import models as jmodels

def random_number_5():
    random.seed()
    ran = str(random.randint(10000, 99999))
    finall_ran = '#'+ran
    return finall_ran

class CharityList(models.Model):
    CHARITY_TYPE = (
        # نماز
        ('نماز واجب', 'نماز واجب'),
        ('نماز مستحب', 'نماز مستحب'),
        ('یک روز کامل', 'یک روز کامل'),
        # قرآن
        ('ختم', 'ختم'),
        ('جزء', 'جزء'),

        ('صلوات', 'صلوات'),
        ('روزه', 'روزه'),
    )
    PRAYER_SUB_TYPE = (
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
    user = PhoneField(help_text='to send sms when charity done...')
    mentioned_info = models.CharField(max_length=128, help_text='نام و نام خانوادگی کسی که برای روح او خیرات انجام می شود.')
    charity_type = models.CharField(max_length=16, choices=CHARITY_TYPE, default=CHARITY_TYPE[0][0])
    prayer_sub_type = models.CharField(max_length=16, choices=PRAYER_SUB_TYPE, blank=True, null=True)
    quantity = models.PositiveSmallIntegerField()
    accepted = models.BooleanField(default=False)
    acceptor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    when_accepted = jmodels.jDateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    purchase_code = models.CharField(max_length=6, default=random_number_5, unique=True)
    created_at = jmodels.jDateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Charity List'
        verbose_name = 'Charity List'

    def __str__(self):
        return self.charity_type

    def save(self, *args, **kwargs):
        self.user = '+98' + str(self.user)
        super().save(*args, **kwargs)





