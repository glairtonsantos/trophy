from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('monsters/', views.MonsterListView.as_view(), name='monster-list'),
    path('coins/collect/', views.CollectCoinCreateView.as_view(), name='collected-coin-create'),
]