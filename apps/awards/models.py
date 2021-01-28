from django.db import models

from .utils import get_choice_all_models

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

class Level(models.Model):
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
    model_class = models.CharField(
        null=False,
        blank=False,
        max_length=50, 
        choice=get_choice_all_models('registers'),
        help_text='anything class to count'
    )
    field = models.CharField(
        null=True,
        blank=True,
        max_length=50, 
        help_text='if want to count anything of a class'
    )
    
    class Meta:
        db_table = 'levels'