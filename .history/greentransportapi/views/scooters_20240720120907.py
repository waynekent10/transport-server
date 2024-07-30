from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from greentransportapi.models import Scooter

class ScooterView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for a single scooter"""
        try:
            scooter = Scooter.objects.get(pk=pk)
            serializer = ScooterSerializer(scooter)
            return Response(serializer.data)
        except Scooter.DoesNotExist:
            return Response({'message': 'Scooter not found'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests for all scooters"""
        scooters = Scooter.objects.all()
        serializer = ScooterSerializer(scooters, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations"""
        scooter = Scooter.objects.create(
            name=request.data["name"],
            model=request.data["model"]
        )
        serializer = ScooterSerializer(scooter)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests"""
        try:
            scooter = Scooter.objects.get(pk=pk)
            scooter.name = request.data["name"]
            scooter.model = request.data["model"]
            scooter.save()
            serializer = ScooterSerializer(scooter)
            return Response(serializer.data)
        except Scooter.DoesNotExist:
            return Response({'message': 'Scooter not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Handle DELETE requests"""
        try:
            scooter = Scooter.objects.get(pk=pk)
            scooter.delete()
            return Response({'message': 'Scooter deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Scooter.DoesNotExist:
            return Response({'message': 'Scooter not found'}, status=status.HTTP_404_NOT_FOUND)

class ScooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scooter
        fields = '__all__'
