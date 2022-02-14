from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from user.models import MyUser
from djongo.models.fields import ObjectIdField

from cloudinary.models import CloudinaryField

from django.db.models.signals import pre_delete
import cloudinary

## models.py
from django.conf import settings

# Add the import for GridFSStorage
from djongo.storage import GridFSStorage

# Create your models here.

grid_fs_storage = GridFSStorage(collection='myfiles', base_url=''.join([settings.BASE_URL, 'myfiles/']))

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
    
    
class ImageModel(models.Model):
    _id = ObjectIdField(primary_key=True, editable=False)
    img = CloudinaryField('image')
    created = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(MyUser, on_delete = models.CASCADE, default= 1)
    
    def __str__(self):
        return str(self.created_by) + ' ' +str(self.img)
    
@receiver(pre_delete, sender=ImageModel)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.img.public_id)