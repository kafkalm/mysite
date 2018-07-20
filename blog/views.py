from django.shortcuts import render
from .models import BlogsPost
# Create your views here.

def blog_index(request):
    blog_list = BlogsPost.objects.all() #获取所有数据
    return render(request,'blog/index.html',{'blog_list':blog_list})
