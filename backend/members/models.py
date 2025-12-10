from django.db import models

# Create your models here.
#tables la rows and columns create
class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    