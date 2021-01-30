
from rest_framework import generics, permissions, response

from .models import TrophyUser
from .serializers import TrophyUserSerializer


class TrophyUserListView(generics.ListAPIView):
    serializer_class = TrophyUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def _get_user(self):
        user = self.request.user

        return user if user and user.is_authenticated else None

    def get_queryset(self):
        user = self._get_user()
        queryset = user.trophies.all()
        return queryset

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return response.Response(serializer.data)
