from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from table.models import Data

User = get_user_model()


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)


class DataTestCases(TestCase):
    def login_user(self):
        self.client.login(
            username='test1',
            password='password',
        )

    def setUp(self) -> None:
        self.user = User.objects.create(username='test1', password='password')
        self.data = Data.objects.create(product='consumer', phone_number='9999999999', author=self.user)
        self.login_user()

    def test_delete_data(self):
        self.data.delete()
        url = reverse('index')
        response = self.client.get(url)
        self.assertNotContains(response, self.data.product)

    def test_create_data(self):
        data = Data.objects.create(product='consumer', phone_number='9999999999', author=self.user)
        url = reverse('index')
        response = self.client.get(url)
        self.assertContains(response, data.product)

