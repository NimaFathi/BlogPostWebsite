from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

# we can use modelForm instead and in view we don't need to create new BlogPost (we can use obj.save())
class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content']    

