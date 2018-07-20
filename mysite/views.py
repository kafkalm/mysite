#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def IndexView(request):
    return render(request,'index.html')