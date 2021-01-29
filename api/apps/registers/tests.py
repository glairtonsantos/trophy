from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, URLPatternsTestCase

from .models import Monster


class KilledMonsterCreateViewTestCase(APITestCase, URLPatternsTestCase):
    urlpatterns = [
            path('', include('apps.registers.urls')),
        ]

    def setUp(self):
        # user authenticate
        self.user = User.objects.create(username='fakeuser')
        self.client.force_login(user=self.user)

        self.monster = Monster.objects.create(name='king-kong')

    def test_create_register_killed_monster(self):
        response = self.client.post(
            reverse('killed-monster-create'),
            data={'user': self.user.id, 'monster': self.monster.id},
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data,
            {
                'id': 1,
                'user': {
                    'id': self.user.id,
                    'name': self.user.username
                },
                'monster': {
                    'id': self.monster.id,
                    'name': self.monster.name
                }
            },
        )

    def test_create_register_killed_monster_required(self):
        response = self.client.post(
            reverse('killed-monster-create'),
            data={'user': self.user.id, 'monster': ''},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data,
            {
                'monster': [
                    'This field may not be null.'
                ]
            },
        )


class DeathCreateViewTestCase(APITestCase, URLPatternsTestCase):
    urlpatterns = [
            path('', include('apps.registers.urls')),
        ]

    def setUp(self):
        # user authenticate
        self.user = User.objects.create(username='fakeuser')
        self.client.force_login(user=self.user)

    def test_create_register_death_user_required(self):
        response = self.client.post(
            reverse('death-create'),
            data={'user': ''},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data,
            {
                'user': [
                    'This field may not be null.'
                ]
            },
        )


class CollectCoinCreateViewTestCase(APITestCase, URLPatternsTestCase):
    urlpatterns = [
            path('', include('apps.registers.urls')),
        ]

    def setUp(self):
        # user authenticate
        self.user = User.objects.create(username='fakeuser')
        self.client.force_login(user=self.user)

    def test_create_register_collected_coin_user_required(self):
        response = self.client.post(
            reverse('collected-coin-create'),
            data={'user': '', 'value': 10},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data,
            {
                'user': [
                    'This field may not be null.'
                ]
            },
        )

    def test_create_register_collected_coin_value_number(self):
        response = self.client.post(
            reverse('collected-coin-create'),
            data={'user': self.user.id, 'value': 'string'},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data,
            {
                'value': [
                    'A valid number is required.'
                ]
            },
        )
