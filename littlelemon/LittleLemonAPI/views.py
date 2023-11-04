from restaurant.views import MenuItemView, SingleMenuItemView, BookingViewSet
from rest_framework import viewsets, permissions
from restaurant.models import *  # the model from Restaurant
from restaurant.serializers import *  # the serializer from Restaurant
from rest_framework.permissions import IsAuthenticated


class APIMenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class APISingleMenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer