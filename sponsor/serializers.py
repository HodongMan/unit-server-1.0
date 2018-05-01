from rest_framework import serializers

from sponsor.models import Sponsor

class SponsorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Sponsor
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