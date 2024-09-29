from django.db import models

# Create your models here.



class Employee(models.Model):
    name = models.CharField(max_length=100)
    

    class Meta:
        verbose_name_plural = 'Employee'
