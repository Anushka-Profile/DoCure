from asyncio.windows_events import NULL
import email
from enum import unique
from pyexpat import model
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User



from django.forms import ModelForm, NullBooleanField, PasswordInput

from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    age=models.IntegerField(null=False, default=0)
    gender=models.CharField(choices=[('Male','Male'),('Female','Female')],max_length=15)
    height=models.IntegerField(null=False, default=0)
    weight=models.IntegerField(null=False, default=0)
    def __str__(self):
        return self.last_name + " " + self.first_name 
    class Meta:  
        db_table = "User"  
        
from django.core.validators import RegexValidator
class Doctor(models.Model):
    username=models.CharField(max_length=100)
    Surname=models.CharField(max_length=100)
    email=models.CharField(max_length=250,unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False) # Validators should be a list
    Specialization=models.CharField(choices=[('Orthopedics','Orthopedics'),(' Internal Medicine',' Internal Medicine'),('Obstetrics and Gynecology','Obstetrics and Gynecology'),('Dermatology','Dermatology'),('Pediatrics','Pediatrics'),('General Surgery','General Surgery')],max_length=50)
    gender=models.CharField(choices=[('Male','Male'),('Female','Female')],max_length=15)
    USERNAME_FIELD = 'username'
    
class ConfirmDoctor(models.Model):
    username=models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username

       
class ViewDoctor(models.Model):
     user=models.ForeignKey(User, on_delete=models.CASCADE)
     doctor=models.ForeignKey(ConfirmDoctor, on_delete=models.CASCADE)
     status = models.IntegerField(null=False, default=0)


class Cbc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rbc = models.FloatField(null=True,blank=True,default=NULL,max_length=150)
    wbc = models.FloatField(blank=True,default=NULL,null=True,max_length=150)
    pc = models.FloatField(null=True,blank=True,default=NULL,max_length=25)
    hgb = models.FloatField(null=True,blank=True,default=NULL,max_length=150)
    rcd= models.FloatField(null=True,blank=True,default=NULL,max_length=150)
    mchc = models.FloatField(null=True,blank=True,default=NULL,max_length=150)
    mpv = models.FloatField(null=True,blank=True,default=NULL,max_length=150)
    pcv = models.FloatField(null=True,blank=True,default=NULL,max_length=150)
    mcv = models.FloatField(null=True,blank=True,default=NULL,max_length=150)
    name= models.CharField(max_length=150,null=True,blank=False)
    password=models.CharField(max_length=150,null=True,blank=True)
    date = models.DateTimeField(default=timezone.now)
class  Comments(models.Model):
     user=models.ForeignKey(User, on_delete=models.CASCADE)
     doctor=models.ForeignKey(ConfirmDoctor, on_delete=models.CASCADE)
     report = models.ForeignKey(Cbc, on_delete=models.CASCADE)
     field_name = models.TextField(max_length=500)
    

