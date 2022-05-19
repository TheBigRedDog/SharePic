from django.db import models
from datetime import datetime
# Create your models here.

class Image(models.Model):
    title=models.CharField('image_title', max_length=100)
    description=models.CharField('image_description', blank=True, max_length=500)
    time_uploaded=models.DateTimeField('upload_time', default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    image=models.ImageField(upload_to='images/')
    
    