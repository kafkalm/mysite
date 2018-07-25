from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogsPost

def IndexView(request):
    blog = BlogsPost.objects.order_by('-date')
    blog_latest = blog[:3]
    blog_return = []
    for i in range(len(blog_latest)):
        blog_return.append(blog_latest[i])
    for i in range(3-len(blog_return)):
        blog_return.append({'text':'暂无内容','title':'暂无内容','date':'暂无内容','keywords':'暂无内容','id':i})
    if 's' in request.GET:
        search = request.GET['s']
        print(search)
        print(type(search))
        result = BlogsPost.objects.filter(title__icontains=search)
        return render(request,'index/search.html',{'search_result':result})
    else:
        return render(request,'index/index.html',{'blog1':blog_return[0],'blog2':blog_return[1],'blog3':blog_return[2],'blog_list':blog_latest})

def AboutusView(request):
    return render(request,'index/aboutus.html')