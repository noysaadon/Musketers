from django.db import models
from .enums import WhoNeedHelpVolunteer, VolunteerType


class User(models.Model):
    username = models.CharField(max_length=10)
    fullname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Company(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    mail = models.CharField(max_length=10)
    website = models.CharField(max_length=10)

    def __str__(self):
        return self.name
