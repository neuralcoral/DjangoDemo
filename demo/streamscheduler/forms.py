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
        fields = ['title', 'description', 'streamer', 'scheduled_time']
        widgets = {
            'scheduled_time': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    def __init__(self, *args, **kwargs):
        super(LiveStreamEventForm, self).__init__(*args, **kwargs)
        mock_user, created = User.objects.get_or_create(username='mockuser', defaults={'password': 'test123'})
        mock_streamer, created = Streamer.objects.get_or_create(user=mock_user, defaults={'display_name':'turbocxnt'})
        self.fields['streamer'].initial = mock_streamer
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
            profile = user.profile
            profile.is_streamer = self.cleaned_data['is_streamer']
            profile.save()
        return user

class StreamerLoginForm(AuthenticationForm):
    pass 
