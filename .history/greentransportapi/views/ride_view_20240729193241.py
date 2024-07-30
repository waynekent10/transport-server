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

    def update(self, request, pk):
        """Handle PUT/PATCH requests to update a ride"""
        try:
            ride = Ride.objects.get(pk=pk)
            ride.user = User.objects.get(id=request.data["user"])
            ride.scooter = Scooter.objects.get(id=request.data["scooter"])
            ride.duration = request.data.get("duration", ride.duration)
            ride.cost = request.data.get("cost", ride.cost)
            ride.save()
            serializer = RideSerializer(ride)
            return Response(serializer.data)
        except Ride.DoesNotExist:
            return Response({'message': 'Ride not found'}, status=status.HTTP_404_NOT_FOUND)

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
