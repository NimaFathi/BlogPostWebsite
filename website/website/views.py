from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    my_title = "Home Page"
    return render(request, "home_page.html", {"title":my_title})


def aboutUs_page(request):
    my_title = "About Us"
    return render(request, "about.html", {"title":my_title})

def contactUs_page(request):
    return render(request, "contact_us.html", {"title":"Contact Us"})

def get_template_example(request):
    context = {"title":"get_template_example"}
    template_name   = "home_page.html"
    template_obj    = get_template(template_name)
    rendered_item   = template_obj.render(context)
    return HttpResponse(redered_item)