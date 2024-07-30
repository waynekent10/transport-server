from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from greentransportapi.models import User, Scooter, Ride
from datetime import datetime

class RideView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for a single ride"""
        try:
            ride = Ride.objects.get(pk=pk)
            serializer = RideSerializer(ride)
            return Response(serializer.data)
        except Ride.DoesNotExist:
            return Response({'message': 'Ride not found'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests for all rides"""
        rides = Ride.objects.all()
        serializer = RideSerializer(rides, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations"""
        user = User.objects.get(id=request.data["user"])
        scooter = Scooter.objects.get(id=request.data["scooter"])
        current_date = datetime.now().date()

        ride = Ride.objects.create(
            user=user,
            scooter=scooter,
            duration=request.data["duration"],
            cost=request.data["cost"]
        )
        serializer = RideSerializer(ride)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def test_update_ride(self):
        """Test updating an existing ride"""
        data = {
            "cost": 15
        }
        response = self.client.put(f'/rides/{self.ride.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cost'], 15)

    def destroy(self, request, pk):
        """Handle DELETE requests to delete a ride"""
        try:
            ride = Ride.objects.get(pk=pk)
            ride.delete()
            return Response({'message': 'Ride deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Ride.DoesNotExist:
            return Response({'message': 'Ride not found'}, status=status.HTTP_404_NOT_FOUND)

class RideSerializer(serializers.ModelSerializer):
    """JSON serializer for post instances"""
    class Meta:
        model = Ride
        fields = ('id', 'user', 'scooter', 'duration', 'cost')
