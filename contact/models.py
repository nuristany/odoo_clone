from django.db import models
import re
from django.core.exceptions import ValidationError

# Create your models here.




class Contact(models.Model):
    
    INDIVIDUAL = 'Individual'
    COMPANY = 'Company'

    CONTACT_TYPE_CHOICES = [
        (INDIVIDUAL, 'Individual'),
        (COMPANY, 'Company')
    ]

    contact_type = models.CharField(max_length=100, choices=CONTACT_TYPE_CHOICES,)
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    address = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name}"
    
    def clean(self):
        if not self.name:
            raise ValidationError("name is required")
        if not re.match(r'^\+?\d{7,15}$', self.phone):
            raise ValidationError('Phone number must contain only digits and be between 7 to 15 characters.')

    
class ContactGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contacts = models.ManyToManyField(Contact, related_name='groups')

    def __str__(self):
        return self.name
