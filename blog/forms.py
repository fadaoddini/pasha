from django import forms

from blog.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'lid', 'description', 'image', 'category', 'status']

        widgets = {'description': forms.Textarea()}


