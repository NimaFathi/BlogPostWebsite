from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost
from django.http import Http404
from .forms import BlogPostForm, BlogPostModelForm
# Create your views here.


# get -> 1 object
#filter -> set of objects
def blog_post_detail_page(request,slug):
    # if slugs wasn't unique:
    #queryset = BlogPost.objects.filter(slug=slug)
    #if queryset.count() == 0:
    #   raise Http404
    #obj = queryset.first()
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name='detail.html'
    context={'object':obj}
    return render(request, template_name, context)


# CRUD


def blog_post_list_view(request):
    queryset = BlogPost.objects.all() # list of python objects
    # as search: queryset = BlogPost.objects.filter(title__icontaints='something here')
    template_name = 'blog/list.html'
    context = {'object_list':queryset}
    return render(request, template_name, context= context)


def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        # obj = BlogPost.objects.create(**form.cleaned_data)
        # we can make some changes to our model with commit = False
        obj = form.save(commit=False)
        obj.title = form.cleaned_data.get("title")
        obj.save()
        form = BlogPostModelForm()
    template_name = 'blog/form.html'
    context = {'form':form}
    return render(request, template_name, context= context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name='blog/detail.html'
    context={'object':obj}
    return render(request, template_name, context)


def blog_post_update_view(request,slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name='blog/update.html'
    context={'object':obj, 'form':''}
    return render(request, template_name, context)


def blog_post_delete_view(request,slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name='blog/delete.html'
    context={'object':obj}
    return render(request, template_name, context)
