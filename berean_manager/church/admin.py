# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from church.models import Member,Department,Family,MemberDepartment,MemberFamily
# Register your models here.


# Register your models here.
admin.site.register(Member)
admin.site.register(Department)
admin.site.register(Family)
admin.site.register(MemberDepartment)
admin.site.register(MemberFamily)