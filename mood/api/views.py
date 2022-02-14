from rest_framework import generics
from mood.models import Mood, FeelingsTag, ReasonsTag, ImageModel
from .serializers import moodSerializer, reasonsTagsSerializer, feelingsTagsSerializer, ImageSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserOrReadOnly

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
        
#######################--------------------- Feelings Tag Model ---------------------#######################
        
class feelingsTagsView(generics.ListCreateAPIView):
        queryset = FeelingsTag.objects.all()
        serializer_class = feelingsTagsSerializer
        permission_classes = [IsAuthenticated]
        
        def perform_create(self, serializer):
            return serializer.save(created_by = self.request.user)
        
        def get_queryset(self):
                user = self.request.user
                userFilter = FeelingsTag.objects.filter(created_by=user)
                adminFilter = FeelingsTag.objects.filter(created_by=1)
                finalFilter = userFilter | adminFilter
                return finalFilter
        
class feelingsTagsDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = FeelingsTag.objects.all()
        serializer_class = feelingsTagsSerializer
        lookup_field = 'id'
        permission_classes = [IsAuthenticated, IsUserOrReadOnly
                              
                              ]
        
        
        
#######################--------------------- Image Model ---------------------#######################

class imageModelView(generics.ListCreateAPIView):
        queryset = ImageModel.objects.all()
        serializer_class = ImageSerializer
        permission_classes = [IsAuthenticated]
        
        def perform_create(self, serializer):
            return serializer.save(created_by = self.request.user)
        
        def get_queryset(self):
                user = self.request.user
                userFilter = Mood.objects.filter(created_by=user).order_by('created')
                return userFilter
        
        
class imageModelDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = ImageModel.objects.all()
        serializer_class = ImageSerializer
        lookup_field = 'id'
        permission_classes = [IsAuthenticated, IsUserOrReadOnly
                              
                              ]