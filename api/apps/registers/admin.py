from django.contrib import admin

from .forms import MonsterForm
from .models import Monster


@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    form = MonsterForm
    search_fields = ['nome']
