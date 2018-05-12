from rest_framework import generics

from .models import Board
from .serializers import BoardSerializer

class BoardList(generics.ListCreateAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'board-list'

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'board-detail'

    def get_obejct(self):

        result = Board.ojbects.get(pk=self.kwargs['pk'])
        result.views += 1
        result.save()

        return result