from django.db import models

# Create your models here.
class TenantDb(models.Model):
    Tenant=models.CharField(max_length=100,blank=True,null=True)
    Phone=models.CharField(max_length=100,blank=True,null=True)
    Email=models.CharField(max_length=100,blank=True,null=True)
    address=models.CharField(max_length=100,blank=True,null=True)

    Document_Proofs=models.ImageField(upload_to="media",blank=True,null=True)
    ImageTenant=models.ImageField(upload_to="media",blank=True,null=True)


class signupdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
