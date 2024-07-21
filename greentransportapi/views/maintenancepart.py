from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from greentransportapi.models import MaintenancePart, Part, Maintenance

class MaintenancePartView(ViewSet):
    def retrieve(self, request, pk):
       try:
        maintenance_part = MaintenancePart.objects.get(pk=pk)
        serializer = MaintenancePartSerializer(maintenance_part)
        return Response(serializer.data)
       except maintenance_part.DoesNotExist:
        return Response({'message': 'Maintenance Part not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        maintenance_parts = MaintenancePart.objects.all()
        serializer = MaintenancePartSerializer(maintenance_parts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        maintenance = Maintenance.objects.get(pk=request.data["maintenance_id"])
        part = Part.objects.get(pk=request.data['part_id'])
        
        maintenance_part = MaintenancePart.objects.create(
            maintenance= maintenance,
            part=part
            
        )

        serializer = MaintenancePartSerializer(maintenance_part)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        
            maintenance_part = MaintenancePart.objects.get(pk=pk)
            maintenance_part.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class MaintenancePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenancePart
        fields = ('id', 'maintenance', 'part')
        depth = 1

    