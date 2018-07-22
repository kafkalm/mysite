#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('',views.IndexView,name = 'index'),
    path('aboutus/',views.AboutusView,name = 'aboutus'),
]