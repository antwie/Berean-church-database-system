from django.conf.urls import include,url
from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views
from church.forms import BioDataForm,ResidenceDataForm
urlpatterns = [
    path('',MembersView, name='welcome'),
    path('login/', auth_views.LoginView.as_view(template_name='church/login.html',redirect_field_name="church/index.html"),name='user_login2'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='church/login.html',redirect_field_name="church/index.html"),name='user_login1'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user/', MembersView, name='members'),
    path('department/', DepartmentView, name='department'),
    path('addMember/',AddMember,name='add_member'),
    path('welcome/',HomeView,name='home'),

    #Add member to form
    path('member/', MemberFormOne, name='first_member_details'),
    path('sacrament/<int:memberID>/',Sacraments,name='sacrament'),
    path('welfare/<int:memberID>/',Welfare_Information,name='welfare'),
    path('addDepartment/<int:memberID>/',AddToDepartment,name='add_department'),

    ]
