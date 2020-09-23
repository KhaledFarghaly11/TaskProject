from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    iD = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField(max_length=50)
    picture = models.ImageField()
    salary = models.CharField(max_length=50)

    def __str__(self):
        return self.name
