from django.db import models

# Create your models here.

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

class Department(models.Model):
    name=models.CharField(max_length=105)
    
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    address=models.TextField(null=True, blank=True)
    age=models.IntegerField()
    number=models.CharField(max_length=15)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}: {self.email}"