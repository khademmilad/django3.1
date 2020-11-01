from django.urls import path
from blog.views import comment_create_form

app_name = 'comment'

urlpatterns = [
    path('create_comment/',comment_create_form,name="create-comment"),

]
