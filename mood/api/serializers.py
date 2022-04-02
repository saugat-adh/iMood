from mood.models import Mood, ReasonsTag, ImageModel
from rest_framework import serializers
from authemail.serializers import UserSerializer

class reasonsTagsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReasonsTag
        fields = '__all__'
        
            
class ImageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
        
    class Meta:
        model = ImageModel
        fields = '__all__'
        
    
class moodSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    reason_tags = reasonsTagsSerializer(many = True, read_only=True)
    
    class Meta:
        model = Mood
        fields = '__all__'