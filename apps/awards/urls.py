from django.urls import path
from rest_framework import routers

from . import views

urlpatterns = [
    path(
        'users/<int:id>/trophies', 
        views.TrophyUserListView.as_view(), 
        name='trophy-user-list'
    ),
]