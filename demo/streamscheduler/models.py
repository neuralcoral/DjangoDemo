from django.db import models
from django.contrib.auth.models import User

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