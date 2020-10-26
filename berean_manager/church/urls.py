from django.conf.urls import include,url
from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views
from church.forms import BioDataForm,ResidenceDataForm
urlpatterns = [
    path('',MembersView, name='members'),
    path('login/', auth_views.LoginView.as_view(template_name='church/login.html',redirect_field_name="church/index.html"),name='user_login2'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='church/login.html',redirect_field_name="church/index.html"),name='user_login1'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user/', MembersView, name='members'),
    path('department/', DepartmentView, name='department'),
    path('addMember/',AddMember,name='add_member'),
    path('member/', MemberFormOne, name='first_member_details'),

    ]
