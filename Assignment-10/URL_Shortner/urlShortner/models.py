from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=10000, unique=True)
    short_link = models.CharField(max_length=10, unique=True)