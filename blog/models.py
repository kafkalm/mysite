from django.db import models

# Create your models here.

class BlogsPost(models.Model):
    title = models.CharField(max_length=150)  #博客标题
    text = models.TextField()                 #博客正文
    date = models.DateTimeField()             #发布时间