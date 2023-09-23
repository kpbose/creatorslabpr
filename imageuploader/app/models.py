from django.db import models
from django.contrib.auth.models import User
class UploadedFile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    nameoffile=models.CharField(max_length=30,null=True,blank=True)
    file = models.FileField(upload_to='uploads/')
