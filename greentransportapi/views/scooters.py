from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from greentransportapi.models import Scooter

class ScooterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Scooter
    fields = ['id', 'name', ]
    depth = 2

class ScooterView(ViewSet):
    def retrieve(self, request, pk):
      try:
        scooter = Scooter.objects.get(pk=pk)
        serializer = ScooterSerializer(scooter, context={'request': request})
        return Response(serializer.data)
      except Scooter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
      scooter = Scooter.objects.all()
      serializer = ScooterSerializer(scooter, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            
            name = request.data['name']

            scooter = Scooter.objects.create(
                name=name,
            )
            serializer = ScooterSerializer(scooter, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Scooter.DoesNotExist:
            return Response({'error': 'Invalid part'}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
      