from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path(
        'monsters/',
        views.MonsterListView.as_view(),
        name='monster-list'
    ),
    path(
        'monsters/kill/',
        views.KilledMonsterCreateView.as_view(),
        name='killed-monster-create'
    ),
    path(
        'coins/collect/',
        views.CollectCoinCreateView.as_view(),
        name='collected-coin-create'
    ),
    path(
        'users/die/',
        views.DeathCreateView.as_view(),
        name='death-create'
    ),
    path(
        'user/detail/',
        views.PanelDetailUserView.as_view(),
        name='panel-detail-user'
    ),
]
