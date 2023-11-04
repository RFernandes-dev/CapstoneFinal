from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_data = [
            {"name": "Item 1", "price": 10},
            {"name": "Item 2", "price": 15},
            {"name": "Item 3", "price": 8},
        ]
        for data in self.menu_data:
            Menu.objects.create(**data)

    # Create a test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_list_menus(self):
        response = self.client.get(reverse('test-menu-item-view'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
        self.assertEqual(response.data, serializer.data)