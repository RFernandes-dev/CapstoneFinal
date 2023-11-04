from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import LittleLemonModelViewSet
from .views import APIMenuView,APISingleMenuView
from rest_framework.permissions import IsAuthenticated


from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'menu-items', APIMenuView, basename='menu-items')
router.register(r'single-menu-item', APISingleMenuView, basename='single-menu-item')

urlpatterns = router.urls
