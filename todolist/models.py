from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    title = models.TextField()
    description = models.TextField()
    finish = models.BooleanField(default=False)
# Create your models here.
