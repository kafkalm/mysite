#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.urls import path
from . import views

app_name = 'index'

urlpattrens = [
    path('',views.IndexView,name = 'index')
]