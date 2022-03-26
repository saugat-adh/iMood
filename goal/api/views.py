from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from goal.models import Goal
from goal.api.serializers import GoalSerializer

class GoalAV(APIView):
    def get(self, request):
        platform= Goal.objects.all()
        serializer = GoalSerializer(platform, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        