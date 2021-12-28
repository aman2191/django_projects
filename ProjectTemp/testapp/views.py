from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Wish(request):
    # return HttpResponse("Welcome you Sir!")
    return render(request,'testapp/wish.html')
