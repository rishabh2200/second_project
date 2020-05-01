from django.shortcuts import render
from .models import jobs

def home(request):
    qwerty=jobs.objects.all()
    return render(request,'jobs/home.html',{'bansal':qwerty})
