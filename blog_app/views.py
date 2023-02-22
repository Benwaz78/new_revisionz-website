from django.shortcuts import render



def home(request):
    return render(request, 'design/index.html')

def about(request):
    return render(request, 'design/about.html')

def services(request):
    return render(request, 'design/services.html')
