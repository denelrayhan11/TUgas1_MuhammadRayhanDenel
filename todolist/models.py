from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    finish = models.BooleanField(default=False)
# Create your models here.
