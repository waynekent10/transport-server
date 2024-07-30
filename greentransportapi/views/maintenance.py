
from greentransportapi.models.maintenance import Maintenance
from greentransportapi.models.scooter import Scooter
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ('id', 'scooter', 'maintenance_date', 'description')
        depth = 2

class MaintenanceView(ViewSet):
    def retrieve(self, request, pk):
        try:
            maintenance = Maintenance.objects.get(pk=pk)
            serializer = MaintenanceSerializer(maintenance, context={'request': request})
            return Response(serializer.data)
        except Maintenance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        maintenances = Maintenance.objects.all()
        serializer = MaintenanceSerializer(maintenances, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):

            scooter = Scooter.objects.get(pk=request.data['scooter_id'])

            maintenance = Maintenance.objects.create(
            scooter=scooter,
            maintenance_date = request.data['maintenance_date'],
            description = request.data['description']
            )
            serializer = MaintenanceSerializer(maintenance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, pk):
        try:
            maintenance = Maintenance.objects.get(pk=pk)
            maintenance.scooter = Scooter.objects.get(pk=request.data['scooter_id'])
            maintenance.maintenance_date = request.data['maintenance_date']
            maintenance.description = request.data['description']
            maintenance.save()

            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Maintenance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Scooter.DoesNotExist:
            return Response({'error': 'Invalid scooter'}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
            maintenance = Maintenance.objects.get(pk=pk)
            maintenance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
