from django.shortcuts import render
from.import forms1,forms2
# Create your views here.
def StudentinputView(request):
    form=forms1.StudentForm()
    form1=forms2.StudentHisForm()
    # context= {
    #     'form':form,'form2':form1
    # }
   
    return render(request,'testapp/input.html',{'form':form,'form2':form1})