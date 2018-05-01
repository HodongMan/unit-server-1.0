from rest_framework import generics

from sponsor.models import Sponsor
from sponsor.serializers import SponsorSerializer

class SpnosorList(generics.ListCreateAPIView):

    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    name = 'spnosor-list'

class SpnosorDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    name = 'sponsor-detail'