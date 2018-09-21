# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import ShowForm
from django.shortcuts import render

# Create your views here.
def show(request):
    form = ShowForm(request.POST or None) 
    if form.is_valid():
        print form.cleaned_data('email')
    context = locals()
    template = 'show.html'
    return render(request,template,context)  
  