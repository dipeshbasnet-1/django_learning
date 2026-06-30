from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Student, Department
from django.contrib import messages
from .forms import StudentForm

# Create your views here.

def home(request):
    students = Student.objects.all() # Select * from student
    paginator=Paginator(students,5)
    page_number = request.GET.get("page")
    page_object=paginator.get_page(page_number)
    
    context={
        "student": students,
        "page_object":page_object
        } 
    
    return render(request, "app/home.html", context)

def student_list(request):
    students = Student.objects.all()
    return render(request, "app/student.html", {"student": students})

def student_detail(request,id):
    student=Student.objects.get(id=id)
    context={
        "student":student
    }
    
    return render(request, "app/student_detail.html",context)

# def add_student(request):
    departments=Department.objects.all()
    
    if request.method=="POST":
        name=request.POST.get("name")
        address=request.POST.get("address")
        email=request.POST.get("email")
        age=request.POST.get("age")
        number=request.POST.get("phone_number")
        department_id=request.POST.get("department")
        
        # Check duplicate email
        if Student.objects.filter(email=email).exists():
            context = {
                "departments": departments,
                "error": "A student with this email already exists."
            }
            return render(request, "app/student_add.html", context)
        department = Department.objects.get(id=department_id)
        
        student =Student(
            name=name,
            address=address,
            email=email,
            age=age,
            number=number,
            department=department,
        )
        student.save()
        
        messages.success(request, "Student added Successfully")
        return redirect("students")
    
    context={
        "departments":departments
    }
    return render (request,"app/student_add.html", context)

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        
        if form.is_valid():
            Student.objects.create(
                name=form.cleaned_data["name"],
                address=form.cleaned_data["address"],
                email=form.cleaned_data["email"],
                age=form.cleaned_data["age"],
                number=form.cleaned_data["number"],
                department = form.cleaned_data["department"]
            )
            
            messages.success(request, "Student added successfully")     # Save student here
            return redirect("students")
    else:
        form = StudentForm()
        
    context = {
        "form": form
    }
    return render(request, "app/student_add.html", context)
    
    
def update_student(request,id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentForm(request.POST)
        
        if form.is_valid() :
            student.name=form.cleaned_data["name"]
            student.address=form.cleaned_data["address"]
            student.email=form.cleaned_data["email"]
            student.age=form.cleaned_data["age"]
            student.number=form.cleaned_data["number"]
            student.department = form.cleaned_data["department"]
            
            student.save()
            messages.success(request, "Student added successfully")     # Save student here
            return redirect("students")
    else:
        form = StudentForm(
            initial={
                "name":student.name,
                "address":student.address,
                "email":student.email,
                "age":student.age,
                "number":student.number,
                "department":student.department,
            }
        )
        
    context = {
        "form": form
    }
    return render(request, "app/update_student.html", context)
    
    
def about(request):
    return render(request, "app/about.html")


def contact(request):
    return render(request, "app/contact.html")


def login(request):
    return render(request, "app/login.html")

