from django.contrib import admin
from .models import BlogsPost
# Register your models here.
class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title','text','date']

admin.site.register(BlogsPost,BlogsPostAdmin)