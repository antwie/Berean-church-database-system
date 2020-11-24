# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.\
class Member(models.Model):

    #personal 
    first_name = models.CharField(max_length = 50,default ='')
    last_name = models.CharField(max_length = 50,default ='')
    other_name = models.CharField(max_length = 50,default ='')
    email = models.EmailField( max_length=150, default='')
    gender = models.CharField(max_length = 20, default = '')
    date_of_birth = models.DateField()

    #residence 
    residence = models.CharField(max_length = 100,default ='')
    house_number = models.CharField(max_length = 50,default ='')
    digital_address = models.CharField(max_length = 50,default ='')
    phone_number = models.CharField(max_length = 15,default ='')
    Home_town = models.CharField(max_length = 100,default ='')
    region = models.CharField(max_length = 100,default ='')
    place_of_birth = models.CharField(max_length = 100,default ='')
    country = models.CharField(max_length = 20, default='Ghana')

    #Sacraments
    baptism = models.CharField(max_length = 20, default='Yes')
    baptism_date = models.CharField(max_length = 50,default ='')
    baptism_place = models.CharField(max_length = 100,default ='')
    date_of_join = models.CharField(max_length = 100,default ='')


    #Welfare Information
    fathers_name = models.CharField(max_length = 50,default ='')
    fathers_location = models.CharField(max_length = 50,default ='')
    mothers_name = models.CharField(max_length = 50,default ='')
    mothers_location = models.CharField(max_length = 50,default ='')


    #Emergency Contact
    emergency_full_name = models.CharField(max_length = 100,default ='')
    emergency_phone = models.CharField(max_length = 50,default ='')
    emergency_address = models.CharField(max_length = 100,default ='')
    emergency_location = models.CharField(max_length = 100,default ='')


    #Matrimony 
    marital_status = models.CharField(max_length = 10,default ='Single')
    Spouse_name = models.CharField(max_length = 100,default ='')
    address = models.CharField(max_length = 100,default ='')
    number_of_children = models.CharField(max_length = 10,default ='0')
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
        return str(self.Member)

    class Meta:
        db_table = "member_department"

