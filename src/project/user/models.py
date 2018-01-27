from django.db import models
from django.contrib.auth.models import User


class Preference(models.Model):
    name = models.CharField(max_length=20)

class Citizen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    city = models.CharField(max_length=100)
    onboard_answer_1 = models.TextField(max_length=300)
    onboard_answer_2 = models.TextField(max_length=300)
    users = models.ManyToManyField(Preference)    
