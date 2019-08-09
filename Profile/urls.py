from django.contrib import admin
from django.urls import path
from . import views
app_name = "Profile"

urlpatterns = [

    path('<str:name>/', views.profile, name = "profile"),
    path('edit/<str:name>/', views.profileEdit, name = "profilEdit")


]
