from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from greentransportapi.models.maintenance import Maintenance
from greentransportapi.models.scooter import Scooter
from django.contrib.auth.models import User

class MaintenanceViewTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser')
        
        self.scooter = Scooter.objects.create(name=1)
        self.maintenance = Maintenance.objects.create(
            scooter=self.scooter,
            maintenance_date='2024-07-01',
            description='Test maintenance'
        )

    def test_retrieve_maintenance(self):
        url = reverse('maintenance-detail', kwargs={'pk': self.maintenance.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Test maintenance')

    def test_list_maintenances(self):
        url = reverse('maintenance-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['description'], 'Test maintenance')

    def test_create_maintenance(self):
        url = reverse('maintenance-list')
        data = {
            'scooter_id': self.scooter.id,
            'maintenance_date': '2024-07-02',
            'description': 'New maintenance'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Maintenance.objects.count(), 2)
        self.assertEqual(response.data['description'], 'New maintenance')

    def test_update_maintenance(self):
        url = reverse('maintenance-detail', kwargs={'pk': self.maintenance.pk})
        data = {
            'scooter_id': self.scooter.id,
            'maintenance_date': '2024-07-03',
            'description': 'Updated maintenance'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.maintenance.refresh_from_db()
        self.assertEqual(self.maintenance.description, 'Updated maintenance')

    def test_destroy_maintenance(self):
        url = reverse('maintenance-detail', kwargs={'pk': self.maintenance.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Maintenance.objects.count(), 0)
