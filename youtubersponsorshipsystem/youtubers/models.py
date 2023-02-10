from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Youtubers(models.Model):
    crew_choice = (
        ('solo' , 'solo'),
        ('small' , 'small'),
        ('medium' , 'medium'),
    )
    camera_choice = (
        ('canon' , 'canon'),
        ('nikon' , 'nikon'),
        ('fuji' , 'fuji'),
    )
    category_choice = (
        ('coder' , 'coder'),
        ('cocking' , 'cocking'),
        ('comedy' , 'comedy'),
    )


    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/youtubers/%y/%m')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choice, max_length=255)
    camera_type = models.CharField(choices = camera_choice, max_length=255)
    sub_count = models.CharField(max_length=255)
    category = models.CharField(choices=category_choice, max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date  = models.DateTimeField(default=datetime.now,blank=True)
 