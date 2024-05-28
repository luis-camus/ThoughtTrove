from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    title = forms.CharField(label='Blog Title',max_length=60, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    content = forms.CharField(label='Content', required=True, widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Blog
        fields = [
            'title',
            'content'
        ]