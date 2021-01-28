from django import forms

from .models import Category, Level, Trophy

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('description',)

class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = (
            'category', 
            'amount', 
            'register_class', 
            'register_field',
        )

class TrophyForm(forms.ModelForm):
    class Meta:
        model = Trophy
        fields = ('category', 'level')