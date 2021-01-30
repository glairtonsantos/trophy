from django.urls import path

from . import views

urlpatterns = [
    path(
        'trophies/',
        views.TrophyUserListView.as_view(),
        name='trophy-user-list'
    ),
]
