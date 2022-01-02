from django import forms
from django.forms import fields
from django.forms.models import ModelMultipleChoiceField
from testapp.models import StudentModelForm

class StudentForm(forms.ModelForm):
    
    allowed_users = ModelMultipleChoiceField(
        label='Allowed Users',
        required=True,
        queryset=StudentModelForm.objects.all()
    )
    account_choices = (("local", "Local"), ("mfsafrica", "Cross border"))
    account_type = forms.ChoiceField(label='Account Type',
                                     widget=forms.Select,
                                     choices=account_choices,
                                     initial="local")
    class Meta:
        model=StudentModelForm
        fields='__all__'
        labels = {
            "name": "Student Name"
        }