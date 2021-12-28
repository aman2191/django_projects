from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
def Creating(request):
    date=datetime.datetime.now()
    dict={'info':{'name':'aman','addr':'Datta Mandir'},
          'sal':{'salary':1000,'year':'2Yr','date':date}
          }
    return render(request,'app2/create.html',context=dict)
