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
    name = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'name-field',
        'placeholder' : 'Enter name ...'
    }))
    email = forms.EmailField(required=False)
    class Meta:
        model = ContactBlog
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if 'milad' in name:
            return name
        else:
            raise forms.ValidationError("Not Valid!")
