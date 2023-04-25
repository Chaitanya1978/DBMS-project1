from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from datetime import date


class Member(AbstractUser):
    member_id = models.AutoField(primary_key=True)
    mobile_number = models.CharField(max_length=12, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=18, null=False, blank=False)

    def __str__(self):
        return str(self.first_name)