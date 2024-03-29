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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from .views import home_page, aboutUs_page, contactUs_page, get_template_example, signIn_page
from blog.views import blog_post_create_view
from searches.views import search_view
urlpatterns = [
    path('', home_page, name='home_page'),
    path('about/', aboutUs_page, name='aboutUs_page'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('blog-new/', blog_post_create_view),
    path('contact/', contactUs_page, name='contactUs_page'),
    path('example/', get_template_example, name="example"),
    path('search/', search_view ),
    path('signIn/' , signIn_page),
    #re_path(r'^blog/(?P<slug>[a-zA-Z-]+)/$', blog_post_detail_page )
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)