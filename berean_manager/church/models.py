# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length = 50,default ='')
    last_name = models.CharField(max_length = 50,default ='')
    phone = models.CharField(max_length = 15,default ='')
    email = models.EmailField( max_length=150, default='')
    place_of_birth = models.CharField(max_length = 100,default ='')
    Home_town = models.CharField(max_length = 100,default ='')
    residence = models.CharField(max_length = 100,default ='')
    marital_status = models.CharField(max_length = 10,default ='')
    gender = models.CharField(max_length = 20, default = '')
    date_of_birth = models.DateField()
    country = models.CharField(max_length = 20, default='Ghana')
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

