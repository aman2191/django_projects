# from django.contrib import admin
from django.urls import path
from testapp.views import Wish 

urlpatterns = [
    path('w/', Wish),
]