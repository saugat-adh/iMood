from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from medication.models import Medications
from .serializers import medicationSerializer

class medicationView(generics.ListCreateAPIView):
    queryset = Medications.objects.all()
    serializer_class = medicationSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
            return serializer.save(created_by = self.request.user)
        
    def get_queryset(self):
                user = self.request.user
                userFilter = Medications.objects.filter(created_by=user)
                return userFilter
            
class medicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medications.objects.all()
    serializer_class = medicationSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]