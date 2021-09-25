from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.
class ContactModelForm(models.Model):
  fullname=models.CharField(max_length=40)
  email=models.EmailField(max_length=100)
  phone=PhoneNumberField()
  msg=models.TextField(max_length=100)

class JoinModelForm(models.Model):
  std_or_tea=[('TEACHER','teacher'),('STUDENT','student')]

  firstname=models.CharField(max_length=100)
  lastname=models.CharField(max_length=100)
  stdortea=models.CharField(max_length=100, choices=std_or_tea)
  email=models.EmailField(max_length=100)
  contactno=PhoneNumberField()

class YourCommentModelForm(models.Model):
  myid=models.IntegerField(primary_key=True, null=False, unique=False)
  username=models.CharField(max_length=100)
  name=models.CharField(max_length=100)
  firstletterofname=models.CharField(max_length=1)
  comment=models.CharField(max_length=500)

class ProfileModel(models.Model):
  myid=models.IntegerField(null=False, primary_key=True, unique=False)
  username=models.CharField(max_length=100)
  firstname=models.CharField(max_length=100)
  lastname=models.CharField(max_length=100)
  email=models.EmailField(max_length=100)
  
  profile=models.ImageField(upload_to='profilepic')

class EnrolledCoursedModelForm(models.Model):
  online_or_offline=[('Online','online'),('Offline','offline')]
  myid=models.IntegerField(primary_key=True, null=False, unique=False)
  username=models.CharField(max_length=100)
  stdfullname=models.CharField(max_length=100)
  stdemail=models.EmailField(max_length=100)
  contactno=PhoneNumberField(default='00000000000')
  onlineoroffline=models.CharField(max_length=10, choices=online_or_offline)
  neet=models.BooleanField()
  jee=models.BooleanField()
  class12=models.BooleanField()
  class11=models.BooleanField()
  class11crashcourse=models.BooleanField()
  class12crashcourse=models.BooleanField()
  class6to10=models.BooleanField()

class FacultymembersDetail(models.Model):
  fmname=models.CharField(max_length=100)
  fmqualification=models.CharField(max_length=10)
  fmspecility=models.CharField(max_length=20)
  fmwords=models.CharField(max_length=200)

  # -----------------------------------------------------------------------------------------------------------------------
  

  

  
  


