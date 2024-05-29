from django.shortcuts import render
from blogs.models import Blog
# Create your views here.
def landing_page(request):
    return render(request, 'main/landingpage.html')

def register_page(request):
    return render(request, 'main/registerpage.html')

def login(request):
    return render(request, 'main/loginpage.html')

def main(request):
    blogs = Blog.objects.all()
    print(blogs)
    return render(request, 'main/mainpage.html', {'blogs': blogs})

