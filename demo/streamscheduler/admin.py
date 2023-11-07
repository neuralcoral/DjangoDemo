from django.contrib import admin
from .models import Streamer, LiveStreamEvent

admin.site.register(Streamer)
admin.site.register(LiveStreamEvent)
