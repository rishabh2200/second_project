from django.shortcuts import render
from .models import blog
# Create your views here.
def allblog(request):
    rishabh=blog.objects.all()
    return render(request,'blog/allblog.html',{'bansal':rishabh})
