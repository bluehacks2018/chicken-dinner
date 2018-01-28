from django.db import models
from django.contrib.auth.models import User

class Preference(models.Model):
    name = models.CharField(max_length=20)

class Citizen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # birthdate = models.DateField()
    city = models.CharField(max_length=100)
    onboard_answer_1 = models.TextField(max_length=300)
    onboard_answer_2 = models.TextField(max_length=300)
    preferences = models.ManyToManyField(Preference) 

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        Citizen.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    instance.citizen.save()
