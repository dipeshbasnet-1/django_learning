from django.shortcuts import render
from .models import Student

# Create your views here.


def home(request):
    students = Student.objects.all() # Select * from student
    context={"student": students} 
    
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


def about(request):
    return render(request, "app/about.html")


def contact(request):
    return render(request, "app/contact.html")


def login(request):
    return render(request, "app/login.html")

'''
Student.objects.all():Select * from student
student.objects.get(id=1): select * from student where id=1 
Student.objects.filter(age=20): select * from student where age=20
Student.objects.create(): insert into Student
Student.delete(): Delete from Student
Student.objects.filter(department_name="BCA")
Student.objects.filter(name_icontains="ram"); like operator or searching pattern
Student.objects.filter(age__gte=18): select * from students where age>=18
Student.objects.filter(age__lte=18): select * from students where age<=25
Student.objects.filter(age__gte=18, age__lte=25): select * from students where age>18 and age >25
Student.objects.filter(age_range=(18,25))
Student.objects.select_related('department').all():
    select * from student join department on student.department_id=department.id where age=20
Student.objects.exclude(age_lte=18)
Student.objects.order_by('name'): ascending order
Student.objects.order_by('-name'): descending order
Student.objects.order_by('name', 'age')
Student.objects.all():[:5]:first five records
Student.objects.all():[5:10]
Student.object.order_by('name').first():
Student.object.order_by('name').last():
'''