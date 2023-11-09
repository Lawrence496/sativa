from distutils.command.upload import upload
from enum import auto
from tabnanny import verbose
from django.db import models

# Create your models here.
class Rooms(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    image4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    class Meta:
        verbose_name_plural = 'Rooms'


