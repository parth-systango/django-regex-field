from django.contrib import admin
from django.urls import path
from regex_field import views

urlpatterns = [
    path('regex/', views.regex),
]
