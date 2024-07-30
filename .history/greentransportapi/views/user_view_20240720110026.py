from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

class UserView(ViewSet):
   def retrieve(self, request, pk):
        """Handle GET requests for a single event"""
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'message': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

class RareUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RareUser
        fields = ['name', 'email', 'username', 'uid']
        depth = 2
