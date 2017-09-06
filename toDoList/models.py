from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Task(models.Model):
    #user = models.ForeignKey(User, blank=False)
    begin = models.DateField(blank=True, default=datetime.now())
    end = models.DateField(blank=True, null=True)
    name = models.CharField(blank=False, max_length=1024)
    is_completed = models.BooleanField(default=False)
