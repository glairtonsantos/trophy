from django.contrib import admin

from .forms import CategoryForm, LevelForm, TrophyForm
from .models import Category, Level, Trophy


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('description',)
    form = CategoryForm
    search_fields = ['description']


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    form = LevelForm


@admin.register(Trophy)
class TrophyAdmin(admin.ModelAdmin):
    form = TrophyForm
