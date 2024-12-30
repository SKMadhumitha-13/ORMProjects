from django.db import models

# Create your models here.

class Country(models.Model):
    Country_no = models.IntegerField()
    Country_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.Country_name

class Capital(models.Model):
    Capital_no=models.IntegerField()
    Capital_name=models.CharField(max_length=100)
    Country_name=models.OneToOneField(Country,on_delete=models.CASCADE)
    def __str__(self):
        return self.Capital_name
    
