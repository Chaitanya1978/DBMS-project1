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

class MemberTasks(models.Model):
    member_task_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, default=1, verbose_name="member", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    due_date = models.DateField(null=False, blank=False)
    is_task_completed = models.BooleanField(default=False)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, default=1, verbose_name="member", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):