from django.db import models
from django.contrib.auth.models import User

class wookname(models.Model):
    website = models.CharField(max_length=100)
    link = models.CharField(max_length =100)
    def __str__(self):
        return self.website
class groupies(models.Model):
    pookname = models.ForeignKey(User, on_delete=models.CASCADE)
    dagroup = models.CharField(max_length=200, default='none')


# Create your models here.
