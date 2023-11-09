from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import DateTimeInput
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from .models import LiveStreamEvent, Streamer
from django.contrib.auth.forms import AuthenticationForm

class LiveStreamEventForm(forms.ModelForm):
    class Meta:
        model = LiveStreamEvent
        fields = ['title', 'description', 'scheduled_time']
        widgets = {
            'scheduled_time': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    def __init__(self, *args, **kwargs):
        super(LiveStreamEventForm, self).__init__(*args, **kwargs)
        self.fields['scheduled_time'].initial = timezone.now()

class CustomUserCreationForm(UserCreationForm):
    is_streamer = forms.BooleanField(required=False, label='Sign up as streamer')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_streamer')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            if self.cleaned_data['is_streamer']:
                Streamer.objects.create(user=user)
            profile = user.profile
            profile.is_streamer = self.cleaned_data['is_streamer']
            profile.save()
        return user

class StreamerLoginForm(AuthenticationForm):
    pass 
