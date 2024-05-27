from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, 'main/landingpage.html')

def register_page(request):
    return render(request, 'main/registerpage.html')

def main(request):
    return render(request, 'main/mainpage.html')