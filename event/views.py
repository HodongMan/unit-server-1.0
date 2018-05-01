from rest_framework import generics

from event.models import Event
from event.serializers import EventSerializer


class EventList(generics.ListCreateAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    name = 'event-list'

class EventDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    name = 'event-detail'