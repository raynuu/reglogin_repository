from django.db import models

# Create your models here.
class registration(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=60)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=30)

class login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    
