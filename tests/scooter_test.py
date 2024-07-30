from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from greentransportapi.models import Scooter
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ScooterViewTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser')
        
        self.scooter = Scooter.objects.create(name=1)

    def test_retrieve_scooter(self):
        url = reverse('scooter-detail', kwargs={'pk': self.scooter.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 1)

    def test_list_scooters(self):
        url = reverse('scooter-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 1)

    def test_create_scooter(self):
        url = reverse('scooter-list')
        data = {
            'name': 2
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Scooter.objects.count(), 2)
        self.assertEqual(response.data['name'], 2)

    def test_create_scooter_missing_field(self):
        url = reverse('scooter-list')
        data = {
            # 'name' is missing
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'Missing required fields')
