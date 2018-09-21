from django.shortcuts import render

# Create your views here.
def home(request):
    context = locals()
    template = 'home.html'
    return render(request,template,context)
    
def behold(request):
    context = locals()
    template = 'behold.html'
    return render(request,template,context)    