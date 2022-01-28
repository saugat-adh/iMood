from django.db import models
from django.contrib.auth.models import User
from user.models import MyUser

# Create your models here.

class ReasonsTag(models.Model):
    name = models.CharField(max_length=20)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default= 1)
    
    def __str__(self):
        return  self.name
    
class FeelingsTag(models.Model):
    name = models.CharField(max_length=20)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default= 1)
    
    def __str__(self):
        return self.name

class Mood(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(MyUser, on_delete = models.CASCADE, default= 1)
    reason_tags = models.ManyToManyField(ReasonsTag)
    feelings_tags = models.ManyToManyField(FeelingsTag)
    
    def __str__(self):
        return self.title + ' BY ' + str(self.created_by)
    
    
    

    