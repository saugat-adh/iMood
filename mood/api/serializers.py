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
        
    def save(self, *args, **kwargs):
        request = self.context.get("request")
        reasonTag = ReasonsTag(name = self.validated_data['name'], created_by = request.user)
        reasonTag.save()
        return reasonTag
        
        

class feelingsTagsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FeelingsTag
        exclude = ('created_by', )
        
    def save(self, *args, **kwargs):
        feelingsTag = FeelingsTag(name = self.validated_data['name'],created_by=self.context['request'].user.id)
        feelingsTag.save()
        return feelingsTag