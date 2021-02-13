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
    print(request.user.username)
    members = Member.objects.all().values()
    # print(members)
    return render(request, 'church/index.html', {"members":members,"heading":"CHURCH MEMBERS"})

# Add a member to the church database
@login_required
def AddMember(request):
    return render(request, 'church/add_member.html',{"heading":"CHURCH MEMBERS"})


@login_required
def DepartmentView(request):
    departmentList = Department.objects.all().values()
    return render(request, 'church/departments.html',{"departments":departmentList,"heading":"CHURCH DEPARTMENTS"})




    
@login_required
def MembersListView(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    # user_id = request.user.id
    # students_in_a_room = StudentRoom.objects.filter(room=roomID)
    # student = Student.objects.filter(studentid=user_id)[0]
    # student_already_has_a_room = StudentRoom.objects.filter(student=student).count() != 0
    # room = Room.objects.filter(id = roomID)[0]
    #print(User.objects.filter(username=)[0])
    # if room.gender == student.gender:
    #     if student_already_has_a_room:
    #         return render(request, 'housing/roommate.html', {"students": students_in_a_room, "roomID": roomID, "has_room":True})
    #     return render(request, 'housing/roommate.html', {"students":students_in_a_room, "roomID": roomID, "has_room":False})
    # else:
    #     return render(request, 'housing/roommate.html', {"students":students_in_a_room, "roomID": roomID, "room":room,"student":student, "has_room":True})

@login_required
def addDepart(request):
    return render(request,"church/add_department.html")

@login_required
def AddToDepartment(request,memberID):
    
    member = Member.objects.filter(id=memberID)[0]
    if request.method == "POST":
        departments = request.POST.getlist('department')
        aux_departments = request.POST.getlist('aux_department')
        groups = request.POST.getlist('groups')

        mega = [departments,aux_departments,groups]

        for i in mega:
            for j in i:
                dep = Department.objects.filter(name=j)[0]
                setMemberDepartment(request,dep,member)
        return HttpResponseRedirect(reverse('members'))
    else:
        return render(request, "Something went wrong")


def setMemberDepartment(request,department_name,member):
    
    try:
        
        _, created = MemberDepartment.objects.update_or_create(
            member = member,
            department = department_name,
            role  = "ggg",
            state = "Active",

        )
        
    except Exception :
            raise Exception

            return render(request,"Something went wrong")

def ImageUpload(request):
    print('image upload',  request.method)
    if request.method == 'POST':
        # get the files with the given name from the html
        files = request.FILES.get('profilepic')
        print(files, request.FILES)
        # store the image in a model rhat has an imagefield instance 
        ImageContainer.objects.create(image=files)
        # redirect to a different page otherwise file keeps saving if user refreshing 
        return render(request, 'church/image_upload.html', {"message": 'image upload was successful'})
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
                
                #Residence Information 
                residence = request.POST.get('residence'),
                house_number = request.POST.get('house_number'),
                digital_address = request.POST.get('digital_address'),
                phone_number = request.POST.get('phone_number'),
                Home_town = request.POST.get('home_town'),
                region = request.POST.get('region'),
                place_of_birth = request.POST.get('place_of_birth'),
                country = request.POST.get('country'),
           
                #Sacraments
                baptism = request.POST.get('baptism'),
                baptism_date = request.POST.get('date_of_baptism'),
                baptism_place = request.POST.get('baptism_place'),
                date_of_join = request.POST.get('date_joined'),

                #Welfare Information
                fathers_name = request.POST.get('father_name'),
                fathers_location = request.POST.get('father_location'),
                mothers_name = request.POST.get('Mother_name'),
                mothers_location = request.POST.get('mother_location'),

                #Matrimony 
                marital_status = request.POST.get('marital_status'),
                Spouse_name = request.POST.get('spouse'),
                address = request.POST.get('current_address'),
                number_of_children = request.POST.get('no_children'),
                name_of_childresn = request.POST.get('name_children'),


                #Emergency Contact
                emergency_full_name = request.POST.get('emergency_name'),
                emergency_phone = request.POST.get('emergency_phone'),
                emergency_address = request.POST.get('emergency_address'),
                emergency_location = request.POST.get('emergency_location'),    
            )
            
            print(_.id)
            return render(request,"church/add_department.html",{"memberID":_.id})
        except Exception :
            raise Exception

            return render(request,"Something went wrong")
    else:
        return render(request, 'authentication/login.html')

class FormWizardView(SessionWizardView):
    template_name = "church/add_member.html"
    form_list = [BioDataForm, ResidenceDataForm]
    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })