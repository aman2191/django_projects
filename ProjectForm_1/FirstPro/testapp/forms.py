from testapp.models import Student
from django import forms

class StudentForm(forms.Form):
    class Meta:
        model=Student
        fields='__all__'