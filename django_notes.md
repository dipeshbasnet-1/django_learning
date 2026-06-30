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

    class Meta:
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
'''
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

Field_options:
    null:True-> database can store null value
    blank:True-> form field can be left empty while submitting form
'''

'''
Student.objects.all():Select * from student
student.objects.get(id=1): select * from student where id=1 
Student.objects.filter(age=20): select * from student where age=20
Student.objects.create(): insert into Student
Student.delete(): Delete from Student
Student.objects.filter(department_name="BCA")
Student.objects.filter(name__icontains="ram"); like operator or searching pattern
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

"""
Filtering:
    filter()
    exclude()
    
Sorting:
    order_by()
    
Limiting:
    slicing[]
    first(),last()
    
Single object:
    get()
    
Aggregation:
    count()
    aggregate()
    Avg()
    Sum()
    Max()
    Min()
    
    EX:
        student.objects.aggregate(avg_age=Avg('age'), total_students=Count('id'))
    
Check:
    exists()
    
Relationship optimization:
    select_related()
    prefetch_related()
"""