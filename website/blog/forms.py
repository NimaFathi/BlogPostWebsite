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

    def clean_title(self, *args, **kwargs):
        cleaned_data = super(BlogPostModelForm, self).clean
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title=title)
        if qs.exists() :
            raise forms.ValidationError("this title has already been used. Please try again with different title")
        return title


