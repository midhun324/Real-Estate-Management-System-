from django.db import models

# Create your models here.

class Property_details(models.Model):

    PropertyName=models.CharField(max_length=50,blank=True,null=True)
    Description=models.CharField(max_length=50,blank=True,null=True)
    Type=models.CharField(max_length=50,blank=True,null=True)
    Address=models.CharField(max_length=50,blank=True,null=True)
    Price=models.CharField(max_length=50,blank=True,null=True)
    Size=models.CharField(max_length=50,blank=True,null=True)
    Parking=models.CharField(max_length=50,blank=True,null=True)
    Garage=models.CharField(max_length=50,blank=True,null=True)
    PropertyStatus=models.CharField(max_length=50,blank=True,null=True)
    PropertyType=models.CharField(max_length=50,blank=True,null=True)
    BedRooms=models.CharField(max_length=50,blank=True,null=True)
    Bathrooms=models.CharField(max_length=50,blank=True,null=True)
    Location=models.CharField(max_length=50,blank=True,null=True)
    Image=models.ImageField(upload_to="media",blank=True,null=True)
    TenantName = models.CharField(max_length=50, blank=True, null=True)