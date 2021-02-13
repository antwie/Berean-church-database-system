# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.\
class Member(models.Model):

    #personal 
    first_name = models.CharField(max_length = 50,default ='' ,blank=True)
    last_name = models.CharField(max_length = 50,default ='' ,blank=True)
    other_name = models.CharField(max_length = 50,default ='' ,blank=True)
    email = models.EmailField( max_length=150, default='' ,blank=True)
    gender = models.CharField(max_length = 20, default = '' ,blank=True)
    date_of_birth = models.DateField()

    #residence 
    residence = models.CharField(max_length = 100,default ='' ,blank=True)  
    house_number = models.CharField(max_length = 50,default ='' ,blank=True)
    digital_address = models.CharField(max_length = 50,default ='' ,blank=True)
    phone_number = models.CharField(max_length = 15,default ='' ,blank=True)
    Home_town = models.CharField(max_length = 100,default ='' ,blank=True)
    region = models.CharField(max_length = 100,default ='' ,blank=True)
    place_of_birth = models.CharField(max_length = 100,default ='' ,blank=True)
    country = models.CharField(max_length = 20, default='Ghana' ,blank=True)

    #Sacraments
    baptism = models.CharField(max_length = 20, default='Yes' ,blank=True)
    baptism_date = models.CharField(max_length = 50,default ='' ,blank=True)
    baptism_place = models.CharField(max_length = 100,default ='' ,blank=True)
    baptism_type = models.CharField(max_length = 100,default ='' ,blank=True)
    date_of_join = models.CharField(max_length = 100,default ='' ,blank=True)


    #Welfare Information
    fathers_name = models.CharField(max_length = 50,default ='' ,blank=True)
    fathers_location = models.CharField(max_length = 50,default ='' ,blank=True)
    father_deceased = models.CharField(max_length = 50,default ='' ,blank=True)
    mothers_name = models.CharField(max_length = 50,default ='' ,blank=True)
    mothers_location = models.CharField(max_length = 50,default ='' ,blank=True)
    mother_deceased = models.CharField(max_length = 50,default ='' ,blank=True)


    #Emergency Contact
    emergency_full_name = models.CharField(max_length = 100,default ='' ,blank=True)
    emergency_phone = models.CharField(max_length = 50,default ='' ,blank=True)
    emergency_address = models.CharField(max_length = 100,default ='' ,blank=True)
    emergency_location = models.CharField(max_length = 100,default ='' ,blank=True)


    #Matrimony 
    marital_status = models.CharField(max_length = 10,default ='Single' ,blank=True)
    Spouse_name = models.CharField(max_length = 100,default ='' ,blank=True)
    address = models.CharField(max_length = 100,default ='' ,blank=True)
    number_of_children = models.CharField(max_length = 10,default ='0' ,blank=True)
    name_of_childresn = models.CharField(max_length = 500,default ='',blank=True)
    
    
    created = models.DateTimeField(default =timezone.now)

    def __str__(self):
        return str(self.first_name)

    class Meta:
        db_table = "member"

class Department(models.Model):
    name = models.CharField(max_length = 100,default ='')
    dep_description = models.CharField(max_length = 500,default ='')

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "Department"

class Family(models.Model):
    name = models.CharField(max_length = 100,default ='')
    family_size = models.IntegerField()

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "Family"


class MemberFamily(models.Model):
    member = models.ForeignKey(Member, on_delete= models.CASCADE)
    family = models.ForeignKey(Family, on_delete= models.CASCADE)

    def __str__(self):
        return str(self.Member)

    class Meta:
        db_table = "member_family"


class MemberDepartment(models.Model):
    member = models.ForeignKey(Member, on_delete= models.CASCADE)
    department = models.ForeignKey(Department, on_delete= models.CASCADE)
    role = models.CharField(max_length = 100,default ='')
    # Active or not Active
    state = models.CharField(max_length = 500,default ='')
    created = models.DateTimeField(default =timezone.now)

    def __str__(self):
        return str(self.member) + str(" -> ")+ str(self.department)

    class Meta:
        db_table = "member_department"

class ImageContainer(models.Model):
    # if you want to link the user id through foreignkey, be my guest
    
    image = models.ImageField(upload_to='images')