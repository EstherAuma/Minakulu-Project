from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self): 
        self.first_name
        

class Data(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    registration_date = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=10, blank=False, null=False)
    occupation = models.CharField(max_length=20, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    nationality = models.CharField(max_length=20, blank=False, null=False)
    district = models.CharField(max_length=20, blank=False, null=False)
    tribe = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=255)

    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        