# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def behold(request):
    context = {}
    template = 'behold.html'
    return render(request,template,context)   
    