from django.http import HttpResponse
from django.shortcuts import render
from .forms import Blogform

def index(request):
    dic = {
        "title" : "django",
        "content" : "some information about django",
        "list" : ["django","milad",124]
    }
    return render(request,'index.html',dic)


def contact(request):
    return render(request,"contact.html",{})



def blog_create_form(request):
    form = Blogform(request.POST)
    if form.is_valid():
        form.save()
        form = Blogform()
    dic = {
        "form" : form
    }
    return render(request,'blog_create.html',dic)
