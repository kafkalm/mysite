from django.shortcuts import render
from django.http import HttpResponse
def IndexView(request):
    #return HttpResponse('Hello')
    return render(request,'index/index.html')
