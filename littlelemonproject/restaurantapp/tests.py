from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Menu
from .serializers import MenuSerializer

# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Steak", price=15, inventory=100)
        self.assertEqual(str(item), "Steak : 15")

class MeneViewTest(TestCase):
    def setup(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="Pasta", price=15, inventory=100)
        self.item2 = Menu.objects.create(title="Noodle", price=12, inventory=100)
        self.item3 = Menu.objects.create(title="Fired Chicken", price=14, inventory=100)
    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)