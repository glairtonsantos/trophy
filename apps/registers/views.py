from django.contrib.auth.models import User
from rest_framework import (filters, generics, pagination, permissions,
                            response, status, viewsets)

from apps.registers.serializers import UserSerializer

from .models import CollectedCoin, Death, KilledMonster, Monster
from .serializers import (CollectCoinCreateSerializer, DeathCreateSerializer,
                          KilledMonsterDetailSerializer,
                          KillMonsterCreateSerializer, MonsterSerializer)


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
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    pagination_class = pagination.PageNumberPagination
    search_fields = ['name']


class CollectCoinCreateView(generics.CreateAPIView):
    """
    Register the collected coin
    """
    queryset = CollectedCoin.objects.all()
    serializer_class = CollectCoinCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class KilledMonsterCreateView(generics.CreateAPIView):
    """
    Register the killed monster
    """
    queryset = KilledMonster.objects.all()
    serializer_class = KillMonsterCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        instance_serializer = KilledMonsterDetailSerializer(
            instance,
            context={'request': request}
        )
        return response.Response(
            instance_serializer.data,
            status=status.HTTP_201_CREATED
        )


class DeathCreateView(generics.CreateAPIView):
    """
    Register death
    """
    queryset = Death.objects.all()
    serializer_class = DeathCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
