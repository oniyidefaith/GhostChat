from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
