from django.db import models
from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class Details(models.Model):
    username = models.CharField(max_length=56)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)


class ChatMessage(models.Model):
    room_name = models.CharField(max_length=255)
    message = models.TextField()
    image = models.ImageField(upload_to='message/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Room: {self.room_name}, Message: {self.message}'
