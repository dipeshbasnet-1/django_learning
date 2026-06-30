from django import forms
from .models import Department

class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Enter name"
        })
    )

    address = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Enter address"
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Enter email"
        })
    )

    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Enter age"
        })
    )

    number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            "placeholder": "Enter phone number"
        })
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="Choose Department",
        widget=forms.Select(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
        })
    )