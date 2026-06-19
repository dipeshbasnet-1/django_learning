from django.shortcuts import render
from .models import Student

# Create your views here.


def home(request):
    students = Student.objects.all()
    context={"student": students}
    
    
    return render(request, "app/home.html", context)

def about(request):
    return render(request, "app/about.html")


def contact(request):
    return render(request, "app/contact.html")


def login(request):
    return render(request, "app/login.html")
