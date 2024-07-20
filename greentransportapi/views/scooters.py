from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from greentransportapi.models import Scooter

class ScooterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Scooter
    fields = ['id', 'name', ]

class ScooterView(ViewSet):
    def retrieve(self, request, pk):
      Scooter = Scooter.objects.get(pk=pk)
      serializer = ScooterSerializer(Scooter, context={'request': request})
      return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
      scooter = Scooter.objects.all()
      serializer = ScooterSerializer(scooter, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
