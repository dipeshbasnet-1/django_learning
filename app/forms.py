from django import forms
from .models import Department, Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
    class Meta:
        model = Student
        fields = [
            "name",
            "address",
            "email",
            "age",
            "number",
            "department",
        ]
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


class CustomUserCreationForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            })
# __init__() runs automatically whenever a form object is created.
# *args  -> accepts any number of positional arguments.
# **kwargs -> accepts any number of keyword arguments (e.g., data=request.POST).
# super().__init__(*args, **kwargs) initializes the original UserCreationForm first.
# After Django creates all the form fields, we loop through them and
# add the same Tailwind CSS classes to every input field.