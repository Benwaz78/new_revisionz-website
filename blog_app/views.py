from django.shortcuts import render
from blog_app.models import *



def home(request):
    return render(request, 'design/index.html')

def about(request):
    about = AboutUs.objects.all()
    return render(request, 'design/about.html', {'abt':about})


def about_detail(request, abt_id):
    detail = AboutUs.objects.get(id=abt_id)
    return render(request, 'design/detail.html', {'det':detail})

def services(request):
    service = ServiceModel.objects.all()
    return render(request, 'design/services.html', {'srv':service})
