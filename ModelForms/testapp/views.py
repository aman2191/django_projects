from django.shortcuts import render
from testapp.forms import StudentForm

# Create your views here.

def StudentView(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
    form=StudentForm()
    return render(request,'testapp/forms.html',{'form':form})
