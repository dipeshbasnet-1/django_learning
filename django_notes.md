# Django Notes

# Basic Commands

Create Project

```bash
django-admin startproject project_name
cd project_name
python manage.py startapp app_name
```

Create App

```bash
python manage.py startapp app_name
```

Run Server

```bash
python manage.py runserver
```

Run Server on another port

```bash
python manage.py runserver 8001
```

Create Migration

```bash
python manage.py makemigrations
```

Apply Migration

```bash
python manage.py migrate
```

Show Migrations
```bash
python manage.py showmigrations
```

Create Superuser
```bash
python manage.py createsuperuser
```

Open Django Shell
```bash
python manage.py shell
```

--------------------------------------

# Register Model in Admin

```python
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

# URL

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
]
```

Dynamic URL
```python
path("student/<int:id>/", views.student_detail, name="student_detail")
```

# Views
Render Template
```python
return render(request, "home.html")
```

Redirect
```python
return redirect("students")
```
Pass Data

```python
context = {
    "students": students
}
return render(request, "home.html", context)
```

# Templates

Variable

```django
{{ student.name }}
```

If Statement

```django
{% if student %}
{% endif %}
```

For Loop

```django
{% for student in students %}
{% endfor %}
```

URL

```django
{% url 'student_detail' student.id %}
```

Static Files

```django
{% load static %}
```

Extends

```django
{% extends "base.html" %}
```

Block

```django
{% block content %}
{% endblock %}
```

Include

```django
{% include "navbar.html" %}
```

CSRF Token

```django
{% csrf_token %}
```

# Forms

Normal Form

```python
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField()
```

Model Form

```python
class StudentForm(forms.ModelForm):

    class META:
        model = Student
        fields = "__all__"
```

# Messages

```python
from django.contrib import messages
```

```python
messages.success(request, "Success")
messages.error(request, "Error")
messages.warning(request, "Warning")
messages.info(request, "Information")
```

# Pagination

```python
from django.core.paginator import Paginator
students = Student.objects.all()
paginator = Paginator(students, 5)
page_number = request.GET.get("page")
page_object = paginator.get_page(page_number)
```

# Shortcuts
```python
render()
redirect()
get_object_or_404()
```

# Authentication
```python
authenticate()
login()
logout()
```

# Common Imports
```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Avg, Count, Sum, Max, Min
from django.core.paginator import Paginator
from django import forms
```

# Static Files
```django
{% load static %}
```

```html
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

# Media Files

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

# Template Inheritance
Parent
```django
{% block content %}
{% endblock %}
```

Child
```django
{% extends "base.html" %}
```

-----------------------------------

# Useful QuerySet Methods
```python
all()
get()
filter()
exclude()
create()
update()
delete()
exists()
count()
first()
last()
order_by()
select_related()
prefetch_related()
aggregate()
values()
values_list()
distinct()
```

# HTTP Methods
```python
GET
POST
PUT
PATCH
DELETE
```

# Request Object

```python
request.method
request.GET
request.POST
request.FILES
request.user
```

# Response
```python
render()
redirect()
HttpResponse()
JsonResponse()
```
# Useful Functions

```python
print()
type()
len()
range()
enumerate()
zip()
sorted()
```
----------------------------------------

## Model Fields

```python
ModelField:
    CharField()
    TextField()
    IntegerField()
    FloatField()
    DecimalField()
    BooleanField()
    DateField()
    TimeField()
    DateTimeField()
    EmailField()
    URLField()
    ImageField()
    FileField()
    ForeignKey()
```

## Field Options

```python
Field_options:
    null=True      # Database can store NULL values.
    blank=True     # Form field can be left empty during form submission.
```

-------------------------------

## Common Django ORM Queries

```python
Student.objects.all()
# SELECT * FROM student;

Student.objects.get(id=1)
# SELECT * FROM student WHERE id=1;

Student.objects.filter(age=20)
# SELECT * FROM student WHERE age=20;

Student.objects.create(...)
# INSERT INTO student (...);

student.delete()
# DELETE FROM student WHERE ...;

Student.objects.filter(department__name="BCA")
# Filter students whose department name is "BCA".

Student.objects.filter(name__icontains="ram")
# Case-insensitive search (LIKE '%ram%').

Student.objects.filter(age__gte=18)
# SELECT * FROM student WHERE age >= 18;

Student.objects.filter(age__lte=25)
# SELECT * FROM student WHERE age <= 25;

Student.objects.filter(age__gte=18, age__lte=25)
# SELECT * FROM student WHERE age >= 18 AND age <= 25;

Student.objects.filter(age__range=(18, 25))
# SELECT * FROM student WHERE age BETWEEN 18 AND 25;

Student.objects.select_related("department").all()
# Performs SQL JOIN to fetch related department in a single query.

Student.objects.exclude(age__lte=18)
# Excludes students whose age is 18 or below.

Student.objects.order_by("name")
# Ascending order.

Student.objects.order_by("-name")
# Descending order.

Student.objects.order_by("name", "age")
# Sort by name, then age.

Student.objects.all()[:5]
# First five records.

Student.objects.all()[5:10]
# Records from index 5 to 9.

Student.objects.order_by("name").first()
# First object after ordering.

Student.objects.order_by("name").last()
# Last object after ordering.
```

---

## QuerySet Operations

### Filtering

```python
filter()
exclude()
```

### Sorting

```python
order_by()
```

### Limiting

```python
[:5]
[5:10]

first()
last()
```

### Retrieving a Single Object

```python
get()
```

### Aggregation

```python
count()
aggregate()

Avg()
Sum()
Max()
Min()
Count()
```

Example:

```python
from django.db.models import Avg, Count

Student.objects.aggregate(
    avg_age=Avg("age"),
    total_students=Count("id")
)
```

### Checking Data

```python
exists()
```

### Relationship Optimization

```python
select_related()
prefetch_related()
```

---------------------------------------

# Adding a Student

## 1. Custom View (Using `request.POST`)

```python
def add_student(request):
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
```

**Notes**
- Uses `request.POST.get()` to retrieve form data.
- Performs validation manually.
- Creates the model object manually.
- Suitable for understanding how Django handles form submissions internally.

---

## 2. Using Django `ModelForm`

```python
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
```

**Notes**
- Uses `StudentForm` (`ModelForm`) for validation.
- Accesses validated data through `cleaned_data`.
- Cleaner and easier to maintain than the custom approach.
- Recommended for most Django applications.

---------------------------------------
## Custom View (request.post)
def add_student(request):
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

This approach manually retrieves form data from `request.POST`, performs validation, creates the model instance, and saves it.

```python
# your custom add_student() function
```

### Features
- Uses `request.POST.get()`
- Manual duplicate email validation
- Manually creates `Student` object
- Good for understanding how form submission works internally

--------------------------------

