from django.contrib import admin
from django.urls import path

from APP2.views import APP2Func1,APP2Func2


urlpatterns = [
    path('a2f1/', APP2Func1),
    path('a2f2/', APP2Func2),

]