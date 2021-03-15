from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    # name=models.CharField(max_length=255)
    email=models.EmailField(blank=True,null=True)
    password=models.CharField(max_length=255,blank=True, null=True)
