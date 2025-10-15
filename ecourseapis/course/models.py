from datetime import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=50, unique= True)

    def __str__(self):
        return self.name

class BaseCourses(models.Model):
    active = models.BooleanField(default= True)
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)

    class Meta:
        abstract = True

class Courses(BaseCourses):
    subject = models.CharField(max_length=255)
    description = models.TextField(null= False)
    image = models.ImageField(upload_to='course/%Y/%m', null= True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
