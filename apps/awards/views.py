
from rest_framework import generics, response

from .models import TrophyUser
from .serializers import TrophyUserSerializer


class TrophyUserListView(generics.ListAPIView):
    serializer_class = TrophyUserSerializer

    def get_queryset(self):
        id = self.kwargs.get('id')
        queryset = TrophyUser.objects.filter(user__pk=id)
        return queryset

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return response.Response(serializer.data)
