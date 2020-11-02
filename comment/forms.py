from django import forms
from .models import Comment
from blog.models import Blog
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder' : 'Write a Comment...'
    }))
    class Meta:
        model = Comment
        fields = [
            'comment',
        ]


# class CommentForm(forms.Form):
#     comment = forms.CharField()
#     name = forms.CharField()
