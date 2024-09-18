from django.db import models
from login.models import Company, User
from login.enums import VolunteerType, WhoNeedHelpVolunteer


class Volunteer(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=700)
    who_need_help = models.PositiveSmallIntegerField(default=WhoNeedHelpVolunteer.CHILD.value, blank=True)
    company = models.ForeignKey(Company, related_name="volunteers", blank=True, on_delete=models.CASCADE, null=True)
    participate = models.ManyToManyField(User, related_name="participate", blank=True)
    type = models.PositiveSmallIntegerField(default=VolunteerType.VOLUNTEER.value, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({VolunteerType(self.type).name})"
