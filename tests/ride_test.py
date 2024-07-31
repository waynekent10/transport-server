# greentransportapi/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from greentransportapi.models import User, Scooter, Ride
from greentransportapi.views.ride_view import RideSerializer

class RideViewTests(APITestCase):

    def setUp(self):
        """Set up for Ride tests"""
        super().setUp()
        # Set up necessary instances for testing
        self.user = User.objects.create(username="testuser")
        self.scooter = Scooter.objects.create(name= 1)
        self.ride = Ride.objects.create(
            user=self.user,
            scooter=self.scooter,
            duration=30,
            cost=10
        )    


    def test_create_ride(self):
        """Test creating a new ride"""
        data = {
            "user": self.user.id,
            "scooter": self.scooter.id,
            "duration": 20,
            "cost": 5
        }
        response = self.client.post('/rides', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['duration'], 20)
        self.assertEqual(response.data['cost'], 5)

    def test_list_rides(self):
        """Test listing all rides"""
        response = self.client.get('/rides')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_ride(self):
        """Test retrieving a single ride"""
        response = self.client.get(f'/rides/{self.ride.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['duration'], self.ride.duration)

    def test_update_ride(self):
        url = reverse('ride-detail', args=[self.ride.id])
        data = {
            'start_time': "2024-07-30T14:00:00Z",
            'end_time': "2024-07-30T15:00:00Z"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.ride.refresh_from_db()
        self.assertEqual(self.ride.start_time, data['start_time'])
        self.assertEqual(self.ride.end_time, data['end_time'])


    def test_update_ride(self):
        """Test updating an existing ride"""
        updated_data = {
            "user": self.user.id,   # Ensure the correct user ID
            "scooter": self.scooter.id,  # Ensure the correct scooter ID
            "duration": 45,
            "cost": 15
        }
        response = self.client.put(f'/rides/{self.ride.id}/', updated_data, format='json')
        
        # Verify the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Fetch the updated ride from the database and verify the changes
        self.ride.refresh_from_db()
        self.assertEqual(self.ride.duration, 45)
        self.assertEqual(self.ride.cost, 15)

        # Optionally verify the response data
        expected_data = RideSerializer(self.ride).data
        self.assertEqual(response.data, expected_data)

    def test_delete_ride(self):
        """Test deleting a ride"""
        response = self.client.delete(f'/rides/{self.ride.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ride.objects.count(), 0)
