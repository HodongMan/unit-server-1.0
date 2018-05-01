from rest_framework import generics

from partner.models import Partner
from partner.serializers import PartnerSerializer

class PartnerList(generics.ListCreateAPIView):

    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    name = 'partner-list'

class PartnerDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    name = 'partner-detail'