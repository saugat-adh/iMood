from django.db import models
from django.dispatch import receiver
from user.models import MyUser
from djongo.models.fields import ObjectIdField

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

import sys

from .Model.script import getEmotion


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
    feelings_tags = models.CharField(max_length=200, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.feelings_tags = getEmotion(str(self.description))
        super(Mood, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title + ' BY ' + str(self.created_by)
    
    
class ImageModel(models.Model):
    _id = ObjectIdField(primary_key=True, editable=False)
    img = models.ImageField(upload_to = 'mood-images')
    created = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(MyUser, on_delete = models.CASCADE, default= 1)
    
    def save(self, *args, **kwargs):
        if not self._id:
            self.img = self.compressImage(self.img)
        super(ImageModel, self).save(*args, **kwargs)
        
    def compressImage(self,uploadedImage):
        imageTemproary = Image.open(uploadedImage)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (1020,573) ) 
        if imageTemproary.mode != 'RGB':
            imageTemproary = imageTemproary.convert('RGB')
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return uploadedImage
    
    def __str__(self):
        return str(self.created_by) + ' ||| ' + str(self.img)
