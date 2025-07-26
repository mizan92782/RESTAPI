from django.db import models

# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    institute = models.CharField(default='PCIU',max_length=100)
    location = models.CharField(default='Bd',max_length=100)
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.name

