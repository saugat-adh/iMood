from mood.models import Mood, ReasonsTag, FeelingsTag
from rest_framework import serializers

class moodSerializer(serializers.ModelSerializer):
    #user = serializers.StringRelatedField(read_only=True)
    #reason_tags = serializers.PrimaryKeyRelatedField(many = True, read_only=True)
    
    class Meta:
        model = Mood
        fields = '__all__'

class reasonsTagsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReasonsTag
        fields = '__all__'
        

class feelingsTagsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FeelingsTag
        fields = '__all__'
        