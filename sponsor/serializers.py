from rest_framework import serializers

from sponsor.models import Sponspor

class SponsporSerializer(serializers.ModelSerializer)

    class Meta:

        model = Sponspor
        fields = (
            'id',
            'division',
            'grade',
            'support_date',
            'support_amount',
            'title',
            'sub_title',
            'department',
            'establish_date',
            'logo_url',
            'slogan',
            'location',
            'description',
            'keyword',
            'email',
            'homepage',

            'created',
        )