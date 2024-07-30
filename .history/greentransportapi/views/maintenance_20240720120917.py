from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from greentransportapi.models import Maintenance

class MaintenanceView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for a single maintenance record"""
        try:
            maintenance = Maintenance.objects.get(pk=pk)
            serializer = MaintenanceSerializer(maintenance)
            return Response(serializer.data)
        except Maintenance.DoesNotExist:
            return Response({'message': 'Maintenance record not found'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests for all maintenance records"""
        maintenances = Maintenance.objects.all()
        serializer = MaintenanceSerializer(maintenances, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations"""
        maintenance = Maintenance.objects.create(
            scooter_id=request.data["scooter_id"],
            description=request.data["description"],
            date=request.data["date"]
        )
        serializer = MaintenanceSerializer(maintenance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests"""
        try:
            maintenance = Maintenance.objects.get(pk=pk)
            maintenance.scooter_id = request.data["scooter_id"]
            maintenance.description = request.data["description"]
            maintenance.date = request.data["date"]
            maintenance.save()
            serializer = MaintenanceSerializer(maintenance)
            return Response(serializer.data)
        except Maintenance.DoesNotExist:
            return Response({'message': 'Maintenance record not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Handle DELETE requests"""
        try:
            maintenance = Maintenance.objects.get(pk=pk)
            maintenance.delete()
            return Response({'message': 'Maintenance record deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Maintenance.DoesNotExist:
            return Response({'message': 'Maintenance record not found'}, status=status.HTTP_404_NOT_FOUND)

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'
