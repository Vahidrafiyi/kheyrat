from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from phone_field.models import PhoneField
from django_jalali.db import models as jmodels

class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'male'
        FEMALE = 'female'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = PhoneField(null=True, blank=True)
    code_melli = models.IntegerField()
    gender = models.CharField(max_length=10, choices=Gender.choices, default=Gender.MALE)
    image = models.ImageField(upload_to='media/images/profile', null=True, blank=True)
    created_at = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.phone = '+98' + str(self.phone)
        super().save(*args, **kwargs)


class Pricing(models.Model):
    CHARITY = [
            ('یک روز کامل', 'یک روز کامل'),
            # قرآن
            ('ختم', 'ختم'),
            ('جزء', 'جزء'),

            ('صلوات', 'صلوات'),

            ('روزه', 'روزه'),
            # نماز واجب
            ('نماز آیات', 'نماز آیات'),
            ('نماز نذر', 'نماز نذر'),
            ('نماز احتیاط', 'نماز احتیاط'),
            ('نماز میت', 'نماز میت'),
            # نماز های مستحب
            ('نماز نافله', 'نماز نافله'),
            ('نماز جعفر طیار', 'نماز جعفر طیار'),
            ('نماز لیله الدفن', 'نماز لیله الدفن'),
            ('نماز شب', 'نماز شب'),
    ]
    charity = models.CharField(max_length=24, choices=CHARITY)
    price = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'pricing'
        verbose_name = 'pricing'

    def __str__(self):
        return self.charity