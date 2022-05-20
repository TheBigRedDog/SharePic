from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Image(models.Model):
    title=models.CharField('Image Title', max_length=100)
    description=models.CharField('Image Description', blank=True, max_length=500)
    time_uploaded=models.DateTimeField('Upload Time', default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    image=models.ImageField(upload_to='images/')
    
    