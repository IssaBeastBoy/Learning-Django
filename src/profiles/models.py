from django.db import models
from django import forms

# Create your models here.
class Profile(models.Model):
    Name = models.CharField(max_length=20, blank=False)
    Surname = models.CharField(max_length=20, blank=False)
    Email = models.EmailField()
    Field = models.CharField(max_length=50, blank=False)
    Institution = models.CharField(max_length=20, blank=False)
    Interest =models.TextField()
    Applications = models.IntegerField(default=0)
    Password = models.CharField(max_length=50,blank=False)
