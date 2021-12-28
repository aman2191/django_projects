from django.shortcuts import render
from testapp.models import Employee

# Create your views here.
def func(request):
    city='Kanpur'
    animal=['cow','goat','pig']
    name_emp=Employee.objects.all()
    context={
        'name':name_emp,
        'city':city,
        'animal':animal
        }
    return render(request,'testapp/testapp.html',context)
