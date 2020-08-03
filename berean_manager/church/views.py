# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.urls import reverse
from .models import Member,Department,Family,MemberDepartment,MemberFamily
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
    return render(request, 'church/index.html')


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
def MemberFormOne(request):
    if request.method == "POST":
        try:
            _, created = Member.objects.update_or_create(
                first_name = request.POST.get('firstname'),
                last_name = request.POST.get('lastname'),
                date_of_birth = "1999-05-05",
                phone= request.POST.get('phone'),
                email = request.POST.get('email'),
                gender= request.POST.get('gender'),
                marital_status = request.POST.get('marital_status'),
                country = request.POST.get('country'),
                Home_town= request.POST.get('home_town'),
                place_of_birth=request.POST.get('pob'),
                residence =request.POST.get('pob'),
                
            )
            
            print(_)
            return HttpResponseRedirect(reverse('members'))
        except Exception :
            raise Exception

            return render(request,"Somethinwrong")
    else:
        return render(request, 'authentication/login.html')

class FormWizardView(SessionWizardView):
    template_name = "church/add_member.html"
    form_list = [BioDataForm, ResidenceDataForm]
    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })