from django.db import models
from apps.registers.models import User
class Category(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        null=False,
        blank=False,
        help_text='identify category',
    )
    description = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        help_text='description category'
    )

    class Meta:
        db_table = 'categories'
    
    def __str__(self):
        return self.description

class Level(models.Model):
    MODELS_CLASS = (
        ('coins', 'CollectedCoin'),
        ('monsters', 'KilledMonster'),
        ('deaths', 'Death'),
    )

    id = models.BigAutoField(
        primary_key=True,
        null=False,
        blank=False,
        help_text='identify category',
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.BigIntegerField(
        null=False,
        blank=False,
        help_text='amount anything',
        default=1
    )
    register_class = models.CharField(
        null=False,
        blank=False,
        max_length=50, 
        choices=MODELS_CLASS,
        help_text='anything class to count'
    )
    register_field = models.CharField(
        null=True,
        blank=True,
        max_length=50, 
        help_text='if want to count anything of a class'
    )
    
    class Meta:
        db_table = 'levels'

    def __str__(self):
        return f'{self.id}: {self.category.description} - {self.amount}'

class Trophy(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        null=False,
        blank=False,
        help_text='identify Trophy',
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    class Meta:
        db_table = 'trophies'
    
    def __str__(self):
        return f'{self.category} - {self.level.amount}'

class TrophyUser(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        null=False,
        blank=False,
        help_text='identify Trophy User',
    )
    trophy = models.ForeignKey(Trophy, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'trophy_user'