from django.contrib.auth.models import User
from rest_framework import serializers

from .models import CollectedCoin, Death, KilledMonster, Monster


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'name')


class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = ('id', 'name')


class CollectCoinCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectedCoin
        fields = ('id', 'value')

    def _get_user(self):
        user = getattr(self.context.get('request'), 'user', None)

        return user if user and user.is_authenticated else None

    def create(self, validated_data):
        user = self._get_user()
        collected_coin = CollectedCoin.objects.create(user=user)

        return collected_coin


class KilledMonsterDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    monster = MonsterSerializer(read_only=True)

    class Meta:
        model = KilledMonster
        fields = ('id', 'user', 'monster')

    def get_user(self, obj):
        user = obj.user
        return {
            'id': user.id,
            'name': user.username
        }


class KillMonsterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = KilledMonster
        fields = ('id', 'monster')

    def _get_user(self):
        user = getattr(self.context.get('request'), 'user', None)

        return user if user and user.is_authenticated else None

    def create(self, validated_data):
        user = self._get_user()
        monster = validated_data['monster']
        killed_monster = KilledMonster.objects.create(
            user=user,
            monster=monster
        )

        return killed_monster


class DeathCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Death
        fields = ('id', 'timestamp')

    def _get_user(self):
        user = getattr(self.context.get('request'), 'user', None)

        return user if user and user.is_authenticated else None

    def create(self, validated_data):
        user = self._get_user()
        death = Death.objects.create(user=user)

        return death
