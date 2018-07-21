from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogsPost

def IndexView(request):
    blog=[]
    for i in BlogsPost.objects.all():
        blog.append(i)
    blog_latest = blog[-3:]
    blog_latest.reverse()
    return render(request,'index/index.html',{'blog1':blog[3],'blog2':blog[1],'blog3':blog[2],'blog_list':blog_latest})
