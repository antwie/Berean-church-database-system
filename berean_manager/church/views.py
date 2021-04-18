# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.urls import reverse
from .models import Member,Department,Family,MemberDepartment,MemberFamily, ImageContainer
from django.contrib.auth.models import User
import csv,io
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate
from .forms import BioDataForm, ResidenceDataForm
from formtools.wizard.views import SessionWizardView

# listing all students in a particular room
# @login_required



@login_required
def LoginView(request):
    return render(request, 'church/home.html')



@login_required
def HomeView(request):
    members = Member.objects.all().values()
    departments = Department.objects.all().values()
    males  = len(Member.objects.filter(gender='Male'))
    females  = len(Member.objects.filter(gender='Female'))
    return render(request, 'church/home.html',{'males':males,'females':females,'members':len(members),'departments':len(departments)})

# List all member in the church
@login_required
def MembersView(request):
    members = Member.objects.all().values()
    return render(request, 'church/index.html', {"members":members,"heading":"CHURCH MEMBERS"})


# Add a member to the church database
@login_required
def AddMember(request):
    return render(request, 'church/add_member.html',{"heading":"CHURCH MEMBERS"})


#Display the list of all departments
@login_required
def DepartmentView(request):
    departmentList = Department.objects.all().values()
    return render(request, 'church/departments.html',{"departments":departmentList,"heading":"CHURCH DEPARTMENTS"})


#View full detail information about a particular member
@login_required
def MembersInfoView(request,memberID):
     member = Member.objects.filter(id=memberID)[0]
     department = MemberDepartment.objects.filter(member=member)
     image = ImageContainer.objects.filter(member=member)
     if len(image) != 0:
         image = image[0]
     return render(request, 'church/profile.html',{"member_info":member,"departments":department,"photo":image})




@login_required
def addDepart(request):
    return render(request,"church/add_department.html")

@login_required
def AddToDepartment(request,memberID):

    member = Member.objects.filter(id=memberID)[0]
    try:
        if request.method == "POST":
            departments = request.POST.getlist('department')
            aux_departments = request.POST.getlist('aux_department')
            groups = request.POST.getlist('groups')

            mega = [departments,aux_departments,groups]

            for i in mega:
                for j in i:
                    dep = Department.objects.filter(name=j)[0]
                    setMemberDepartment(request,dep,member)
            return render(request,"church/image_upload.html",{"memberID":memberID})
    except Exception :

        return render(request,"Something went wrong")
    else:
        return render(request, 'authentication/login.html')



@login_required
def setMemberDepartment(request,department_name,member):
    try:
        _, created = MemberDepartment.objects.update_or_create(
            member = member,
            department = department_name,
            role  = "None",
            state = "Active",

        )
    except Exception :
            raise Exception
            return render(request,"Something went wrong")



@login_required
def Sacraments(request,memberID):

    member = Member.objects.filter(id=memberID)[0]
    if request.method == "POST":
        try:
            #Sacraments
            member.baptism = request.POST.get('baptism')
            member.baptism_date = request.POST.get('date_of_baptism')
            member.baptism_place = request.POST.get('baptism_place')
            #member.date_of_join = request.POST.get('date_joined')
            member.baptism_type = request.POST.get('baptism_type')
            member.save()
            return render(request,"church/welfare.html",{"memberID":memberID})
        except Exception :
            raise Exception

            return render(request,"Something went wrong")
    else:
        return render(request, 'authentication/login.html')



@login_required
def Welfare_Information(request,memberID):
    member = Member.objects.filter(id=memberID)[0]
    if request.method == "POST":
        try:
            #Welfare Information
            member.fathers_name = request.POST.get('father_name')
            member.fathers_location = request.POST.get('father_location')
            member.father_deceased = request.POST.get('fatherAliveorDead')
            member.mothers_name = request.POST.get('Mother_name')
            member.mothers_location = request.POST.get('mother_location')
            member.mother_deceased = request.POST.get('motherAliveorDead')

            #Matrimony
            member.marital_status = request.POST.get('marital_status')
            member.Spouse_name = request.POST.get('spouse')
            #member.address = request.POST.get('current_address')
            member.number_of_children = request.POST.get('no_children')
            member.name_of_childresn = request.POST.get('name_children')

            #Emergency Contact
            member.emergency_full_name = request.POST.get('emergency_name')
            member.emergency_phone = request.POST.get('emergency_phone')
            member.emergency_address = request.POST.get('emergency_address')
            member.emergency_location = request.POST.get('emergency_location')


            member.save()
            return render(request,"church/add_department.html",{"memberID":memberID})
        except Exception :
            raise Exception

            return render(request,"Something went wrong")
    else:
        return render(request, 'authentication/login.html')

@login_required
def ImageUpload(request,memberID):
   #
    print('image upload',  request.method)
    member = Member.objects.filter(id=memberID)[0]
    if request.method == 'POST':
        # get the files with the given name from the html
        files = request.FILES.get('profilepic')
        print(files, request.FILES)
        # store the image in a model that has an imagefield instance
        ImageContainer.objects.create(image=files,member=member)
        # redirect to a different page otherwise file keeps saving if user refreshing
        return render(request, 'church/home.html', {"message": 'image upload was successful'})
    return render(request, 'church/image_upload.html', {"message": ''})




@login_required
def MemberFormOne(request):
    if request.method == "POST":
        try:
            _, created = Member.objects.update_or_create(
                #Personal Information
                first_name = request.POST.get('firstname'),
                last_name = request.POST.get('lastname'),
                other_name = request.POST.get('lastname'),
                email =request.POST.get('email'),
                gender = request.POST.get('gender'),
                date_of_birth = request.POST.get('dob'),
                date_joined = request.POST.get('date_joined'),
                occupation = request.POST.get('occupation'),
                #Residence Information
                residence = request.POST.get('residence'),
                house_number = request.POST.get('house_number'),
                digital_address = request.POST.get('digital_address'),
                phone_number = request.POST.get('phone_number'),
                Home_town = request.POST.get('home_town'),
                region = request.POST.get('region'),
                place_of_birth = request.POST.get('place_of_birth'),
                country = request.POST.get('country'),
                landmark = request.POST.get('landmark'),

            )


            return render(request,"church/sacrament.html",{"memberID":_.id})
        except Exception :
            raise Exception

            return render(request,"Something went wrong")
    else:
        return render(request, 'authentication/login.html')
