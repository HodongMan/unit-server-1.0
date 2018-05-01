from rest_framework import generics

from sponsor.models import Sponspor
from sponsor.serializers import SponsorSerializer

class SpnosorList(generics.ListCreateAPIView):

    queryset = Sponspor.objects.all()
    serializer_class = SponsorSerializer
    name = 'spnosor-list'

class SpnosorDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Sponspor.objects.all()
    serializer_class = SponsorSerializer
    name = 'sponsor-detail'