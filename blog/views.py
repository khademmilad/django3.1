from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    dic = {
        "title" : "django",
        "content" : "some information about django",
        "list" : ["django","milad",124]
    }
    return render(request,'index.html',dic)


def contact(request):
    return render(request,"contact.html",{})
