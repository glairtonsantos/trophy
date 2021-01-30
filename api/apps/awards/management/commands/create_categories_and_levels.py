from django.core.management.base import BaseCommand, CommandError

from ...models import Category, Level, Trophy

CATEGORIES = [
    ('coins', 'número de moedas coletadas'),
    ('monsters', 'número de monstros que matou'),
    ('deaths', 'número de vezes que morreu')
]

LEVELS_AMOUNT = [
    100,
    1000,
    10000,
    100000
]

DEATHS_AMOUNT = [10, 25, 50, 100]


class Command(BaseCommand):
    help = 'Create all categories, levels and trophies'

    def create_level(self, category_obj, class_choice):
        if class_choice != 'deaths':
            for amount in LEVELS_AMOUNT:

                level_data = {
                    'category': category_obj,
                    'amount': amount,
                    'register_class': class_choice
                }

                if class_choice == 'monsters':
                    level_data['register_field'] = 'monster.name'

                level = Level.objects.create(**level_data)
        else:
            for amount in DEATHS_AMOUNT:
                level = Level.objects.create(
                    category=category_obj,
                    amount=amount,
                    register_class=class_choice
                )

        Trophy.objects.create(category=category_obj, level=level)

    def create_categories(self):
        for category in CATEGORIES:
            category_obj = Category.objects.create(description=category[1])
            self.create_level(category_obj, category[0])

    def handle(self, *args, **options):
        try:
            self.create_categories()
            print('Done! 3 categories and 5 levels created for all category!')
        except Category.ObjectDoesNotExist:
            raise CommandError('Ops! Somethins went wrong here.')
