from django.db import models

# Create your models here.
class usuario(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    google_auth_code = models.CharField(max_length=16)
