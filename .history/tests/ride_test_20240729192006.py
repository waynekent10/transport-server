# greentransportapi/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from greentransportapi.models import User, Scooter, Ride
from greentransportapi.views.ride_view import RideSerializer

class RideViewTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create(name='John Doe', email='john@example.com', username='johndoe', uid='12345')
        self.scooter = Scooter.objects.create(name='Scooter A', model='Model A', battery_level=100)
        self.ride = Ride.objects.create(user=self.user, scooter=self.scooter, duration=30, cost=10)
        self.ride2 = Ride.objects.create(user=self.user, scooter=self.scooter, duration=45, cost=15)

    def test_retrieve_ride(self):
        url = reverse('ride-detail', args=[self.ride.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = RideSerializer(self.ride).data
        self.assertEqual(response.data, expected_data)

    def test_list_rides(self):
        url = reverse('ride-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = RideSerializer([self.ride, self.ride2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_create_ride(self):
        url = reverse('ride-list')
        data = {
            'user': self.user.pk,
            'scooter': self.scooter.pk,
            'duration': 20,
            'cost': 8
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ride.objects.count(), 3)
        self.assertEqual(Ride.objects.get(pk=response.data['id']).duration, 20)

    def test_update_ride(self):
        url = reverse('ride-detail', args=[self.ride.pk])
        data = {
            'user': self.user.pk,
            'scooter': self.scooter.pk,
            'duration': 35,
            'cost': 12
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.ride.refresh_from_db()
        self.assertEqual(self.ride.duration, 35)
        self.assertEqual(self.ride.cost, 12)

    def test_partial_update_ride(self):
        url = reverse('ride-detail', args=[self.ride.pk])
        data = {
            'duration': 40
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.ride.refresh_from_db()
        self.assertEqual(self.ride.duration, 40)

    def test_delete_ride(self):
        url = reverse('ride-detail', args=[self.ride.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ride.objects.count(), 1)
