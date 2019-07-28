from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost
from django.http import Http404
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
    template_name='blog_post_detail.html'
    context={'object':obj}
    return render(request, template_name, context)


# CRUD


def blog_post_list_view(request):
    queryset = BlogPost.objects.all() # list of python objects
    template_name = 'blog_post_list.html'
    context = {'object_list':queryset}
    return render(request, template_name, context= context)


def blog_post_create_view(request):
    template_name = 'blog_post_create.html'
    context = {'form':''}
    return render(request, template_name, context= context)


def blog_post_detail_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name='blog_post_detail.html'
    context={'object':obj}
    return render(request, template_name, context)


def blog_post_update_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name='blog_post_update.html'
    context={'object':obj, 'form':''}
    return render(request, template_name, context)


def blog_post_delete_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name='blog_post_delete.html'
    context={'object':obj}
    return render(request, template_name, context)
