from django.http import Http404
from django.shortcuts import render, redirect
from .models import LiveStreamEvent, Profile
from .forms import LiveStreamEventForm, CustomUserCreationForm, StreamerLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

EVENTS = {
    1: {'title': 'Test Event', 'description': 'This is a test event', 'streamer': 'Streamer Name', 'scheduled_time': '2023-11-06 20:00:00'},
}


class StreamerLoginView(LoginView):
    template_name = 'login.html'
    form_class = StreamerLoginForm

def event_detail(request, pk):
    # event = LiveStreamEvent.objects.get(pk=pk)
    event = EVENTS.get(pk)
    if event is None:
        raise Http404('Event not found.')
    return render(request, 'event_detail.html', {'event': event})


def schedule_list(request):
    events = LiveStreamEvent.objects.all().order_by('scheduled_time')
    return render(request, 'schedule_list.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        form = LiveStreamEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = LiveStreamEventForm()
    return render(request, 'create_event.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})