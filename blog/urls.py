#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.blog_index,name='index'),
]