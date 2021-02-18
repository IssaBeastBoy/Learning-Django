from django.db import models

# Create your models here.
class Profile(models.Model):
    Name = models.CharField(max_length=20, blank=False)
    Surname = models.CharField(max_length=20, blank=False)
    Field = models.CharField(max_length=20, blank=False)
    Institution = models.CharField(max_length=20, blank=False)
    Interest =models.TextField()
    Applications = models.TextField()
    