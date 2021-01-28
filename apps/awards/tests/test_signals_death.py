from django.test import TestCase
from model_mommy import mommy

from apps.registers.models import Death

from ..models import Category, Level, Trophy


class CollectedCoinSignalsTestCase(TestCase):
    def setUp(self):
        self.user = mommy.make('User')

    def test_register_if_user_win_trophy_death(self):
        category = Category.objects.create(description='numbers deaths user')
        level = Level.objects.create(
            category=category,
            amount=1,
            register_class='deaths'
        )
        trophy_death = Trophy.objects.create(
            category=category,
            level=level
        )

        # user death
        Death.objects.create(user=self.user)

        trophies = self.user.trophies.filter(trophy=trophy_death).exists()

        # verify if user has trophy death
        self.assertTrue(trophies)

    def test_register_if_user_win_trophy_death_others_levels(self):
        category = Category.objects.create(description='numbers deaths user')

        # create others levels
        for amount in [10, 25, 50, 100]:
            level = Level.objects.create(
                category=category,
                amount=amount,
                register_class='deaths'
            )
            Trophy.objects.create(
                category=category,
                level=level
            )

        # user died 100 times
        for coin in range(100):
            Death.objects.create(user=self.user)

        trophies = self.user.trophies.filter(trophy__category=category)

        # verify if user has 4 trophy coin
        self.assertEqual(trophies.count(), 4)
