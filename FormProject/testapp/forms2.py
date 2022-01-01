from django import forms

class StudentHisForm(forms.Form):
    education=forms.CharField()
    