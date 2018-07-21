#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.BlogIndex,name='index'),
    path('detail/<int:pk>/',views.BlogDetails.as_view(),name='detail'),
    path('list/<int:page>/',views.BlogList,name='list'),
]