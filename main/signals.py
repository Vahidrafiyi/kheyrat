from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import Profile
from main.models import Fast, Prayer, Salavat, Quran, CharityList

@receiver(post_save, sender=Fast)
def charity_notification(sender, created, instance, **kwargs):
    if created:
        CharityList.objects.create(charity_type='fast', quantity=instance.how_many, accepted=False)

@receiver(post_save, sender=Prayer)
def charity_notification(sender, created, instance, **kwargs):
    if created:
        CharityList.objects.create(charity_type='prayer', quantity=instance.how_many, accepted=False)

@receiver(post_save, sender=Quran)
def charity_notification(sender, created, instance, **kwargs):
    if created:
        CharityList.objects.create(charity_type='quran', quantity=instance.how_many, accepted=False)

@receiver(post_save, sender=Salavat)
def charity_notification(sender, created, instance, **kwargs):
    if created:
        CharityList.objects.create(charity_type='salavat', quantity=instance.how_many, accepted=False)

# @receiver(post_save, sender=CharityList)
# def charity_for_user(sender, created, instance, **kwargs):
#     if instance.accepted:
#         Profile.objects.get(user=)
