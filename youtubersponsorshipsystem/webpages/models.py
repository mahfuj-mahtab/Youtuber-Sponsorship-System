from django.db import models

# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    button_text = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='media/slider/%y/')
    created_date = models.DateField(auto_now_add = True)


# this function will solve object name problem in admin panel
    def __str__(self):
        return self.headline




class Team(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='media/slider/%y/%m')
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add = True)


# this function will solve object name problem in admin panel
    def __str__(self):
        return self.firstname