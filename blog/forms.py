from django import forms
from .models import Blog

class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            "title",
            "content"
        ]


class Contactform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    content = forms.Textarea()
