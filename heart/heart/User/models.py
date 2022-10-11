from django.db import models
from .import models

# Create your models here.
class register(models.Model):
      fname=models.CharField(max_length=90)
      lname=models.CharField(max_length=90)
      uname=models.CharField(max_length=90)
      email=models.CharField(max_length=90)
      password=models.CharField(max_length=90)
      confirmpassword=models.CharField(max_length=90)