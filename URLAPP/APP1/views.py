from django import http
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def App1Func1(request):
    return HttpResponse("This is APP1 Func1")

def App1Func2(request):
    return HttpResponse("Thai is APP1 Func2")
