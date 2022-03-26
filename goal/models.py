from django.db import models
from django.contrib.auth.models import User
from user.models import MyUser
# Create your models here.
class Goal(models.Model):
    GOALS_CHOICES = (
        ("Daily", "Dailygoals"),
        ("Weekly", "Weeklygoals"),
        ("Monthly", "Monthlygoals"),
    )
    topic = models.CharField(max_length=20)
    discussion = models.CharField(max_length=20)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default= 1)
    goals_type= models.CharField(max_length=9, choices=GOALS_CHOICES, default="Daily"  )
    
    def __str__(self):
        return  self.topic
    