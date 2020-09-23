from django import forms
from PIL import Image


class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    iD = forms.CharField()
    email = forms.EmailField()
    picture = forms.FileField()
    salary = forms.CharField()
