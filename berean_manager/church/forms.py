# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms


class BioDataForm(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    other_name = forms.CharField(max_length=100)
    phone = forms. CharField(max_length=100)
    dob = forms.DateField()
    email = forms.EmailField()
    gender = forms.CharField(max_length=10)
    marriage_status = forms.CharField(max_length=10)

class ResidenceDataForm(forms.Form):
    place_of_recidence  = forms.CharField(max_length=100)
    home_town = forms.CharField(max_length=100)
    Country = forms.CharField(max_length=100)
    place_of_birth = forms. CharField(max_length=100)
