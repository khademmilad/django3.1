from django import forms
from .models import Blog,ContactBlog

class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            "title",
            "content"
        ]

#
# class Contactform(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     content = forms.Textarea()


class ContactBlogForm(forms.ModelForm):
    class Meta:
        model = ContactBlog
        fields = '__all__'
