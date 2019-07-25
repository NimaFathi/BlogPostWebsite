from django.db import models

# Create your models here.


class BlogPost(models.Model):
    # id = models.IntegerField() or pk
    title = models.CharField(max_length=50)
    slug = models.SlugField() # hello world -> hello-world
    content = models.TextField(null=True, blank=True)
    


