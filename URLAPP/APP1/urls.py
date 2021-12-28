from django.contrib import admin
from django.urls import path

from APP1.views import App1Func1,App1Func2

urlpatterns = [
    path('a1f1/', App1Func1),
    path('a1f2/', App1Func2),
    ]