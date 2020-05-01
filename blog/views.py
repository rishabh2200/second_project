from django.shortcuts import render,get_object_or_404
from .models import blog
# Create your views here.
def allblog(request):
    rishabh=blog.objects.all()
    return render(request,'blog/allblog.html',{'bansal':rishabh})

def detail(request,blog_id):
    rishabh=get_object_or_404(blog,pk=blog_id)
    return render(request,'blog/detail.html',{'bansal':rishabh})
