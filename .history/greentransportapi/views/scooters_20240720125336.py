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
        try:
            scooter = Scooter.objects.get(pk=pk)
            serializer = ScooterSerializer(scooter, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Scooter.DoesNotExist:
            return Response({'message': 'Scooter not found'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        scooters = Scooter.objects.all()
        serializer = ScooterSerializer(scooters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ScooterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
