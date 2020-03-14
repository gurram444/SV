from django import forms
from .models import *


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
