# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from testapp.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=('name','lname','roll')
admin.site.register(Student,StudentAdmin)
