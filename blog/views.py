from django.shortcuts import render
from .models import BlogsPost
from django.views import generic
# Create your views here.

def BlogIndex(request):
    blog_list = BlogsPost.objects.all()
    blognum = list(range(1,(BlogsPost.objects.count())//11+2))  #每10篇博客分一页
    return render(request,'blog/index.html',{'blog_list':blog_list,'blog_num':blognum})

def BlogList(request,page):
    blog_list = BlogsPost.objects.all()
    blognum = list(range(1, (BlogsPost.objects.count()// 11 ) + 2))  # 每10篇博客分一页
    return render(request, 'blog/index.html', {'blog_list': blog_list, 'blog_num': blognum,'page':page})

class BlogDetails(generic.DetailView):
    model = BlogsPost
    template_name = 'blog/blogdetail.html'
    context_object_name = 'blog'