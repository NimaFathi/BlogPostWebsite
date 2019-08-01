from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
    my_title = "Home Page"
    qs = BlogPost.objects.all()[:5]
    context={
        "title":"Home Page",
        "blog_list":qs,
        }
    return render(request, "home_page.html", context)


def aboutUs_page(request):
    my_title = "About Us"
    return render(request, "about.html", {"title":my_title})

def contactUs_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    form = ContactForm()
    context = {
        "title":"Contact Us",
        "form":form
    }
    return render(request, "form.html", context=context)

def get_template_example(request):
    context = {"title":"get_template_example"}
    template_name   = "home_page.html"
    template_obj    = get_template(template_name)
    rendered_item   = template_obj.render(context)
    return HttpResponse(rendered_item)