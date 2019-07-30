from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects #blog 안의 데이터를 나타내는 변수
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail}) #있으면 object를 가져오고 없으면 404에러

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now() #시간을 자동으로 불러옴
    blog.save() 
    return redirect('/blog/'+str(blog.id)) #내용처리 후 해당 url로 이동
# Create your views here.
