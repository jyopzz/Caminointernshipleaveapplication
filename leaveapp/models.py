from distutils.command.upload import upload
import email
from email.policy import default
from unicodedata import name
from django.db import models

# Create your models here.

#emp leaveapply   starting
class Leaveapply(models.Model):
    name=models.CharField(max_length=100)
    empid=models.CharField(max_length=100)
    startingdate=models.CharField(max_length=100 ,default='' ,null=False )
    endingdate=models.CharField(max_length=100 ,default='' ,null=False)
    reason=models.CharField(max_length=200)

#emp leaveapply   starting


#admin leavedetails   starting
class Leavedetails(models.Model):
    userid=models.TextField(max_length=15 ,default="" ,null=True)
    name=models.CharField(max_length=100)
    empid=models.CharField(max_length=100)
    startingdate=models.CharField(max_length=100,default='' ,null=False)
    endingdate=models.CharField(max_length=100,default='' ,null=False)
    reason=models.CharField(max_length=200)
    status=models.CharField(max_length=100)

#admin leavedetails   ending

#admin  admindata starting
class Admindata(models.Model):
    image=models.ImageField(null=True,blank=True)
    #image=models.ImageField(upload_to='profile_images/',blank=True,null=True)
    name=models.CharField(max_length=100)
    adminid=models.CharField(max_length=100)  
    jobtitle=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=11)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    repassword=models.CharField(max_length=100)

#admin  admindata ending

