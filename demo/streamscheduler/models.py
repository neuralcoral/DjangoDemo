from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Streamer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)

    def __str__(self):
        return self.display_name

class LiveStreamEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    streamer = models.ForeignKey(Streamer, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_streamer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s profile"