from django.http import HttpResponse
from django.shortcuts import render
from .forms import Blogform,ContactBlogForm
from .models import Blog

def index(request):
    obj = Blog.objects.get(pk=1)
    dic = {
        "title" : obj.title,
        "content" : obj.content
    }
    return render(request,'index.html',dic)


# def contact(request):
#     if request.method == "POST":
#         form = Contactform(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data.get("name")
#             email = form.cleaned_data.get("email")
#         print(name,email)
#         print(form.cleaned_data)
#     else:
#         form = Contactform()
#
#     dic = {
#         "form" : form
#         }
#
#     return render(request,"contact.html",dic)

def contact(request):
    form = ContactBlogForm()
    if request.method == "POST":
        form = ContactBlogForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactBlogForm()

    dic = {
    'form' : form
    }
    return render(request, "contact.html",dic)



def blog_create_form(request):
    form = Blogform(request.POST)
    if form.is_valid():
        form.save()
        form = Blogform()
    dic = {
        "form" : form
    }
    return render(request,'blog_create.html',dic)
