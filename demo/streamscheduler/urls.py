from django.contrib import admin
from django.urls import path
from .views import event_detail, schedule_list


urlpatterns = [
    path('', schedule_list, name='schedule_list'),
    path('events/<int:pk>', event_detail, name='event_detail'),
]
