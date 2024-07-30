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
   def list(self, request):
        """Handle GET requests to get all events"""
        events = Event.objects.all()
        uid = request.META['HTTP_AUTHORIZATION']
        gamer = Gamer.objects.get(uid=uid)

        for event in events:
                # Check to see if there is a row in the Event Games table that has the passed in gamer and event
                event.joined = len(EventGamer.objects.filter(
                    gamer=gamer, event=event)) > 0    


        serializer = EventSerializer(events, many=True)
        return Response(serializer.data) 
