"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from .views import home_page, aboutUs_page, contactUs_page, get_template_example
from blog.views import blog_post_detail_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('about/', aboutUs_page, name='aboutUs_page'),
    path('contact/', contactUs_page, name='contactUs_page'),
    path('example/', get_template_example, name="example"),
    path('blog/<str:slug>/', blog_post_detail_page ),
    #re_path(r'^blog/(?P<slug>[a-zA-Z-]+)/$', blog_post_detail_page ),
    #we can use this easier:
]
