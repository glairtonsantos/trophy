from rest_framework import serializers

from .models import Category, Level, Trophy, TrophyUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'description')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'amount', 'register_class', 'register_field')


class TrophySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    level = LevelSerializer(read_only=True)

    class Meta:
        model = Trophy
        fields = ('id', 'category', 'level')


class TrophyUserSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    trophy = TrophySerializer(read_only=True)

    class Meta:
        model = TrophyUser
        fields = ('id', 'user', 'trophy', 'value_register_field')

    def get_user(self, obj):
        user = obj.user
        return {
            'id': user.id,
            'name': user.username
        }
