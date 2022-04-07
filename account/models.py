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
    gender = models.CharField(max_length=10, choices=Gender.choices, default=Gender.MALE)
    image = models.ImageField(upload_to='media/images/profile', null=True, blank=True)
    fast = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    salavat = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    prayer = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    quran = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    created_at = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username