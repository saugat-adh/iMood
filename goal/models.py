from django.db import models
from django.contrib.auth.models import User
from user.models import MyUser
# Create your models here.
class DailyGoal(models.Model):
    topic = models.CharField(max_length=20)
    discussion = models.CharField(max_length=20)
    date_time = models.DateTimeField()
    
    def __str__(self):
        return  self.topic