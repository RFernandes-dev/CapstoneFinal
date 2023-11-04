from django.test import TestCase
from restaurant.models import Menu

#TestCase class
class MenuItemTest(TestCase):
     def test_get_item(self):
        item = Menu.objects.create(name="IceCream", price=80, menu_item_description= "A delicious ice cream filled with chocolate biscuits")
        self.assertEqual(str(item), "IceCream : 80")
