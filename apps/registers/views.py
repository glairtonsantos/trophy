from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, generics, filters, pagination
from apps.registers.serializers import UserSerializer
from .serializers import MonsterSerializer
from .models import Monster
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class MonsterListView(generics.ListAPIView):
    """
    List all paginated monsters
    """
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = pagination.PageNumberPagination
    search_fields = ['name',]