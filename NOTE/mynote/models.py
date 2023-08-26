from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.TextField(blank=True)
    name1=models.CharField(max_length=128, null=True)
    age=models.CharField(max_length=128, null=True)

    
    def __str__(self):
        return self.name1