from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from greentransportapi.models import MaintenancePart, Part, Maintenance

class MaintenancePartView(ViewSet):
    def retrieve(self, request, pk):
       try:
        maintenancepart = MaintenancePart.objects.get(pk=pk)
        serializer = MaintenancePartSerializer(maintenancepart)
        return Response(serializer.data)
       except maintenancepart.DoesNotExist:
        return Response({'message': 'Maintenance Part not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        maintenanceparts = MaintenancePart.objects.all()
        serializer = MaintenancePartSerializer(maintenanceparts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        maintenance = Maintenance.objects.get(pk=request.data["maintenance_id"])
        part = Part.objects.get(pk=request.data['part_id'])
        
        maintenancepart = MaintenancePart.objects.create(
            maintenance= maintenance,
            part=part
            
        )

        serializer = MaintenancePartSerializer(maintenancepart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        
            maintenancepart = MaintenancePart.objects.get(pk=pk)
            maintenancepart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class MaintenancePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenancePart
        fields = ('id', 'maintenance', 'part')
        depth = 1

    