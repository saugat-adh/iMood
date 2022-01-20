from rest_framework import serializers
from medication.models import Medications

class medicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Medications
        fields = '__all__'