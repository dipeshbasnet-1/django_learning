from django import forms
from .models import Department, Student

class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Enter name",
            "id":"name",
        })
    )

    address = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Enter address",
            "id":"address",
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Enter email",
            "id":"email",
        })
    )

    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Enter age",
            "id":"age",
        })
    )

    number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Enter phone number",
            "id":"number",
        })
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="Choose Department",
        widget=forms.Select(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
        })
    )
    
class StudentModelForm(forms.ModelForm):
    class META:
        model = Student
        fields=['name','address','email','age','number','department']
        # fields='__all__'
        # exclude = []
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none",
                "placeholder": "Enter name",
            }),
            
            "address": forms.TextInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none",
                "placeholder": "Enter address",
            }),
            
            "email": forms.EmailInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none",
                "placeholder": "Enter email",
            }),
            
            "age": forms.NumberInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none",
                "placeholder": "Enter age",
            }),
            
            "number": forms.TextInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none",
                "placeholder": "Enter phone number",
            }),
            
            "department": forms.Select(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2 bg-white focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none",
            }),
        }
        