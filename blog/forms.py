from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'name':'body', 'rows':10, 'cols':50,'class':'form-control'}),
        } 
        labels = {
            'title' : 'Title',
            'content' : 'Content',
        }
        

