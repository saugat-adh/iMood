from django.db import models
from user.models import MyUser
import django.utils.timezone

# Create your models here.

class Medications(models.Model):
    name = models.CharField(max_length=20)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default= 0)
    dosage = models.IntegerField()
    time = models.TimeField()
    date = models.DateTimeField(auto_now_add=True)
    INTAKE_CHOICES = (
        ("Once Daily", "DailyIntake"),
        ("Twice Daily", "Twice DailyIntake"),
        ("Other", "Any other"),
    )
    intake_type= models.CharField(max_length=20, choices=INTAKE_CHOICES, default="Once Daily"  )
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default= 1)
    
    def __str__(self):
        return self.name