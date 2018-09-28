# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
# Create your views here.
def contact(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None) 
    confirm_message = None
    

    if form.is_valid():
        name = form.cleaned_data('name')
        comment = form.cleaned_data('comment')
        subject = 'Message from laart.info'
        message = '%s %s' %(comment, name) 
        fromEmail = form.cleaned_data('email')
        toEmail = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, fromEmail, toEmail, fail_silently=False)
        title = "Thank You!"
        confirm_message = "We appreciate your interest and will get back to you shortly."
        form = None
    context = {'title': title,'form': form, 'confirm_message': confirm_message}
    template = 'contact.html'
    return render(request,template,context)  