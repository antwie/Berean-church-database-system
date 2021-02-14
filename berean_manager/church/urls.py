from django.conf.urls import include,url
from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views
from church.forms import BioDataForm,ResidenceDataForm
urlpatterns = [
    path('',HomeView, name='welcome'),
    path('login/', auth_views.LoginView.as_view(template_name='church/login.html',redirect_field_name="church/home.html"),name='user_login2'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='church/login.html',redirect_field_name="church/home.html"),name='user_login1'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('welcome/',HomeView,name='home'),
    path('user/', MembersView, name='members'),
    path('department/', DepartmentView, name='department'),
    path('addMember/',AddMember,name='add_member'),
    

    #Add member to form
    path('member/', MemberFormOne, name='first_member_details'),
    path('sacrament/<int:memberID>/',Sacraments,name='sacrament'),
    path('welfare/<int:memberID>/',Welfare_Information,name='welfare'),
    path('image/<int:memberID>/', ImageUpload, name='upload_image'),
    path('addDepartment/<int:memberID>/',AddToDepartment,name='add_department'),


    #View details of a member
    path('member/<int:memberID>/', MembersInfoView, name='memberDetails'),

    ]
