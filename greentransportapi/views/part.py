from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from greentransportapi.models import Part

class PartView(ViewSet):
    def retrieve(self, request, pk):
      Part = Part.objects.get(pk=pk)
      serializer = PartSerializer(Part, context={'request': request})
      return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
      part = Part.objects.all()
      serializer = PartSerializer(part, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        try:
            
            part_name = request.data['part_name']
            part_number = request.data['part_number']

            part = Part.objects.create(
                part_name=part_name,
                part_number=part_number,
            )
            serializer = PartSerializer(part, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Part.DoesNotExist:
            return Response({'error': 'Invalid part'}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        """Handle DELETE requests to delete a user"""
        try:
            part = Part.objects.get(pk=pk)
            part.delete()
            return Response({'message': 'Part deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Part.DoesNotExist:
            return Response({'message': 'Part not found'}, status=status.HTTP_404_NOT_FOUND)
  
class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ['id', 'part_name', 'part_number']
        depth = 2