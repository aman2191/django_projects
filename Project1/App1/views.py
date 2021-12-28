# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def display(response):
    s="<h1> Aman LOVE Supriya</h1>"
    return HttpResponse(s)