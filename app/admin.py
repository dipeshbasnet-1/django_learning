from django.contrib import admin
from .models import Student, Department


# Register your models here.

# admin.site.register(Student)
# admin.site.register(Department)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields=["name"]
    ordering=["name"]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=("id", "name", "email", "address", "age", "number", "department" )
    
    search_fields=["name", "email", "age"]
    ordering=["name", "age"]