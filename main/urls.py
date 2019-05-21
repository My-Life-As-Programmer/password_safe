from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage,name="home"),
    path('search/', views.user_homepage,name="search"),
    path('server_details/<slug:name>', views.server_details,name="server_details"),
    path('server_details/', views.server_details,name="server_details"),
    #path('login/', views.user_login,name="login"),
    path('login/', auth_views.LoginView.as_view(template_name='main/user_login.html'),name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/user_logout.html'),name="logout"),
    path('user_home', views.user_homepage,name="user_home"),
    path('logs/', views.view_logs,name="logs"),

]
