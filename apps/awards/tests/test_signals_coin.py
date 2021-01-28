from django.test import TestCase
from model_mommy import mommy

from apps.registers.models import CollectedCoin

from ..models import Category, Level, Trophy


class CollectedCoinSignalsTestCase(TestCase):
    def setUp(self):
        self.user = mommy.make('User')

    def test_register_if_user_win_trophy_coin(self):
        category = Category.objects.create(
            description='numbers collected coins'
        )
        level = Level.objects.create(
            category=category,
            amount=1,
            register_class='coins'
        )
        trophy_coin = Trophy.objects.create(
            category=category,
            level=level
        )

        # user collected coin
        CollectedCoin.objects.create(user=self.user, value=10)

        trophies = self.user.trophies.filter(trophy=trophy_coin).exists()

        # verify if user has trophy coin
        self.assertTrue(trophies)

    def test_register_if_user_win_trophy_coin_others_levels(self):
        category = Category.objects.create(
            description='numbers collected coins'
        )

        # create others levels
        for amount in [100, 1000, 10000, 100000]:
            level = Level.objects.create(
                category=category,
                amount=amount,
                register_class='coins'
            )
            Trophy.objects.create(
                category=category,
                level=level
            )

        # user collected 1000 coins
        for coin in range(1000):
            CollectedCoin.objects.create(user=self.user, value=10)

        trophies = self.user.trophies.filter(trophy__category=category)

        # verify if user has 2 trophy coin
        self.assertEqual(trophies.count(), 2)
