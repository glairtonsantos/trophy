
from rest_framework import generics, permissions, response
from .serializers import TrophyUserSerializer
from .models import TrophyUser
class TrophyUserListView(generics.ListAPIView):
    serializer_class = TrophyUserSerializer

    def get_queryset(self):
        id = self.kwargs.get('id')
        queryset = TrophyUser.objects.filter(user__pk=id) 
        return queryset

    def get(self, request, *args, **kwargs):
            
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return response.Response(serializer.data)
