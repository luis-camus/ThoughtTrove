from django.shortcuts import render, HttpResponse
from .forms import BlogForm
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return HttpResponse("data is saved in database")
        else:
            pass
    form = BlogForm()
    return render(request, 'main/writeblog.html', {'form': form})