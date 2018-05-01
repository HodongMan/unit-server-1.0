from rest_framework import serializers

from partner.models import Partner

class PartnerSerializer(serializers.ModelSerializer)

    class Meta:

        model = Partner
        fields = (
            'id',
            'division',
            'grade',
            'activity',
            'title',
            'sub_title',
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