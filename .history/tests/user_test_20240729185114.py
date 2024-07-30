# greentransportapi/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from greentransportapi.models import User
from greentransportapi.views.user_view import UserSerializer

class UserViewTests(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create(name='John Doe', email='john@example.com', username='johndoe', uid='12345')
        self.user2 = User.objects.create(name='Jane Smith', email='jane@example.com', username='janesmith', uid='67890')

    def test_retrieve_user(self):
        url = reverse('user-detail', args=[self.user1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = UserSerializer(self.user1).data
        self.assertEqual(response.data, expected_data)

    def test_list_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = UserSerializer([self.user1, self.user2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'name': 'Alice Wonderland',
            'email': 'alice@example.com',
            'username': 'alice',
            'uid': '54321'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)
        self.assertEqual(User.objects.get(pk=response.data['id']).name, 'Alice Wonderland')

    def test_update_user(self):
        url = reverse('user-detail', args=[self.user1.pk])
        data = {
            'name': 'John Updated',
            'email': 'johnupdated@example.com',
            'username': 'johnupdated',
            'uid': '12345'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.name, 'John Updated')
        self.assertEqual(self.user1.email, 'johnupdated@example.com')
        self.assertEqual(self.user1.username, 'johnupdated')

    def test_partial_update_user(self):
        url = reverse('user-detail', args=[self.user1.pk])
        data = {
            'name': 'John Partial Update'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.name, 'John Partial Update')

    def test_delete_user(self):
        url = reverse('user-detail', args=[self.user1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 1)
