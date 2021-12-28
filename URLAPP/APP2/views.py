from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def APP2Func1(request):
    print("##############")
    # print(__file__)
    return HttpResponse("This is APP2 Func1")

def APP2Func2(request):
    return HttpResponse("this is APP2 Func2")
