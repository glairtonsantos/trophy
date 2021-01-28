from django.test import TestCase
from model_mommy import mommy

from apps.registers.models import KilledMonster, Monster

from ..models import Category, Level, Trophy


class KilledMonsterSignalsTestCase(TestCase):
    def setUp(self):
        self.user = mommy.make('User')

    def test_register_if_user_win_trophy_killed_monster(self):
        category = Category.objects.create(
            description='numbers killed monsters'
        )
        level = Level.objects.create(
            category=category,
            amount=1,
            register_class='monsters',
            register_field='monster.name'
        )
        trophy_killed_monster = Trophy.objects.create(
            category=category,
            level=level
        )

        monster_godzilla = Monster.objects.create(name='godzilla')
        monster_kingkong = Monster.objects.create(name='king-kong')

        # user killed 2 monsters differents
        KilledMonster.objects.create(user=self.user, monster=monster_godzilla)
        KilledMonster.objects.create(user=self.user, monster=monster_kingkong)

        trophies = self.user.trophies.filter(trophy=trophy_killed_monster)

        # verify if user has trophy monster
        self.assertTrue(trophies.exists())

        # verify if user has 2 trophy monsters
        self.assertEqual(trophies.count(), 2)

    def test_register_if_user_win_trophy_killed_monster_others_levels(self):
        category = Category.objects.create(
            description='numbers killed monsters'
        )

        # create others levels
        for amount in [100, 1000, 10000, 100000]:
            level = Level.objects.create(
                category=category,
                amount=amount,
                register_class='monsters',
                register_field='monster.name'
            )
            Trophy.objects.create(
                category=category,
                level=level
            )

        monster_godzilla = Monster.objects.create(name='godzilla')
        monster_kingkong = Monster.objects.create(name='king-kong')

        # user kill 1000 monsters (type)
        for coin in range(1000):
            # user killed 2 monsters differents
            KilledMonster.objects.create(
                user=self.user,
                monster=monster_godzilla
            )
            KilledMonster.objects.create(
                user=self.user,
                monster=monster_kingkong
            )

        trophies = self.user.trophies.filter(trophy__category=category)
        trophies_godzilla = trophies.filter(
            value_register_field=monster_godzilla.name
        )
        trophies_kingkong = trophies.filter(
            value_register_field=monster_kingkong.name
        )

        # verify if user has 4 trophy /2 monsters
        self.assertEqual(trophies.count(), 4)
        self.assertEqual(trophies_godzilla.count(), 2)
        self.assertEqual(trophies_kingkong.count(), 2)
