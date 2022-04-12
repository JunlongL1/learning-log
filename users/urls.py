"""为应用程序users定义URL模式"""

from re import template
from django.urls import re_path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "users"

urlpatterns = [
    #登陆页面
    re_path(r'^login/$', LoginView.as_view(template_name = 'users/login.html'), name='login'),
    re_path(r'^logout/$', views.logout_view, name = 'logout'),
    #注册页面
    re_path(r'^register/$', views.register, name='register'),
]