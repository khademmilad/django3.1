from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .forms import Blogform,ContactBlogForm
from .models import Blog
from django.views.generic import ListView
from comment.models import Comment,ReplyComment

class BlogList(ListView):
    template_name = 'index.html'
    queryset = Blog.objects.all()


# def index(request):
#     queryset = Blog.objects.all()
#     dic = {
#         'posts' : queryset
#     }
#     return render(request,'index.html',dic)


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


def detail_view(request,my_id):
    # obj = Blog.objects.get(pk=my_id)
    obj = get_object_or_404(Blog,pk=my_id)
    # get comment from Comment with pk
    comments = Comment.objects.filter(blog_id=my_id)
    is_active = True
    # get re_comment from ReplyComment with comment's id
    re_comments = []
    for comment in comments:
        c_id = comment.id
        re_comments.append(ReplyComment.objects.filter(comment_id=c_id))

    dic = {
        "object" : obj,
        "comments":comments,
        "is_active":is_active,
        "re_comments":re_comments
    }
    print(re_comments)

    return render(request,"detail.html",dic)



def delete_post(request,my_id):
    obj = get_object_or_404(Blog, pk=my_id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request,"delete_post.html")
