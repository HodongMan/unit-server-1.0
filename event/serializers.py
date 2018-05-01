from rest_framework import serializers

from event.models import Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:

        model = Event
        fields = (
            'id',
            'host',
            'division',
            'image_url',
            'register_start',
            'register_end',
            'event_start',
            'event_end',
            'location',
            'description',
            'keyword',
            'homepage',

            'created',
        )