from django.shortcuts import render

# Create your views here.


def home(request):
    
    subject=[
        "Python",
        "Java",
        "MySql",
        "C++"
    ]
    context = {
        "name":"Dipesh",
        "age":20,
        "city":"Kathmandu",
        "subjects":subject
    }
    
    return render(request, "app/home.html", context)

def about(request):
    return render(request, "app/about.html")


def contact(request):
    return render(request, "app/contact.html")


def login(request):
    return render(request, "app/login.html")
