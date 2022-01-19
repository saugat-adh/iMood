from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerilizers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'password2',]
        extra_kwargs = {'password' : {'write_only' : True,}}
        
    def save(self, *args, **kwargs):
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'error' : 'P1 and P2 Should Be Same'})
        
        
        if User.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError({'error' : 'Email already exists'})
        
        
        account = User(email = self.validated_data['email'], username = self.validated_data['username'])
        account.set_password(password)
        account.save()
        
        return account