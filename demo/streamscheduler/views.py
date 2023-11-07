from django.http import Http404
from django.shortcuts import render
from .models import LiveStreamEvent

EVENTS = {
    1: {'title': 'Test Event', 'description': 'This is a test event', 'streamer': 'Streamer Name', 'scheduled_time': '2023-11-06 20:00:00'},
}

def event_detail(request, pk):
    # event = LiveStreamEvent.objects.get(pk=pk)
    event = EVENTS.get(pk)
    if event is None:
        raise Http404('Event not found.')
    return render(request, 'event_detail.html', {'event': event})


def schedule_list(request):
    events = LiveStreamEvent.objects.all().order_by('scheduled_time')
    return render(request, 'schedule_list.html', {'events': events})