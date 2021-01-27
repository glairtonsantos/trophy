from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Monster, CollectedCoin
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = ['id', 'name']

class CollectCoinCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectedCoin
        fields = ('id', 'value', 'user')

    def _get_user(self):
        user = getattr(self.context.get('request'), 'user', None)

        return user if user and user.is_authenticated else None

    def create(self, validated_data):
        user = self._get_user()
        collected_coin = CollectedCoin.objects.create(user=user)

        return collected_coin