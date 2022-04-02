from rest_framework import generics
from mood.models import Mood, ReasonsTag, ImageModel
from .serializers import moodSerializer, reasonsTagsSerializer, ImageSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserOrReadOnly
from bson.objectid import ObjectId

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from mood.Model.script import getEmotion

#######################--------------------- Mood Model ---------------------#######################

class MoodView(generics.ListCreateAPIView):
        queryset = Mood.objects.all()
        serializer_class = moodSerializer
        permission_classes = [IsAuthenticated]
        
        def perform_create(self, serializer):
            return serializer.save(created_by = self.request.user)
        
        def get_queryset(self):
                user = self.request.user
                userFilter = Mood.objects.filter(created_by=user).order_by('created')
                return userFilter

class MoodDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Mood.objects.all()
        serializer_class = moodSerializer
        lookup_field = 'id'
        permission_classes = [IsAuthenticated, IsUserOrReadOnly]
        
        
#######################--------------------- Reason Tag Model ---------------------#######################

class reasonsTagsView(generics.ListCreateAPIView):
        queryset = ReasonsTag.objects.all()
        serializer_class = reasonsTagsSerializer
        permission_classes = [IsAuthenticated]
        
        def perform_create(self, serializer):
            return serializer.save(created_by = self.request.user)
        
        
        def get_queryset(self):
                user = self.request.user
                userFilter = ReasonsTag.objects.filter(created_by=user)
                adminFilter = ReasonsTag.objects.filter(created_by=1)
                finalFilter = userFilter | adminFilter
                return finalFilter
        
class reasonsTagsDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = ReasonsTag.objects.all()
        serializer_class = reasonsTagsSerializer
        lookup_field = 'id'
        permission_classes = [IsAuthenticated, IsUserOrReadOnly]
                
        
######################--------------------- Image Model ---------------------#######################

class imageModelView(generics.ListCreateAPIView):
        serializer_class = ImageSerializer
        permission_classes = [IsAuthenticated, IsUserOrReadOnly]
        
        def perform_create(self, serializer):
                return serializer.save(created_by = self.request.user)
                
                
        def get_queryset(self):
                user = self.request.user
                id = self.request.query_params.get('id', None)
                userFilter = ImageModel.objects.filter(created_by=user)
                if id == None:
                        return userFilter
                else:
                        return ImageModel.objects.filter(_id=ObjectId(id), created_by=user)
     

class deleteImage(APIView):        
        permission_classes = [IsAuthenticated, IsUserOrReadOnly]
          
        def delete(self, request):
                if request.method == 'DELETE':
                        id = self.request.query_params.get('id', None)
                        if id == None:
                                return Response(status=status.HTTP_404_NOT_FOUND)
                        else:
                                file = ImageModel.objects.filter(_id=ObjectId(id))
                                file.delete()
                                return Response({"detail":"File was deleted"},status=status.HTTP_200_OK)
        
        