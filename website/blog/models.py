from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q
# Create your models here.

User = settings.AUTH_USER_MODEL

#how to get users: from django.contrib.auth import get_user_model
# j = User.onjects.first : (first user)
# to take all BlogPosts: j.blogpost_set.all()

class BlogPostQuerySet(models.QuerySet):
    # objects.all().published
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)
    def search(self , query):
        lookup = (
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(slug__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(user__username__icontains=query) |
                Q(user__email__icontains=query)
        )
        return self.filter(lookup)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)
        # objects.published()
    def published(self):
        return self.get_queryset().published()
    def search(self, query = None):
        if query is None:
            return self.get_queryset().none
        return self.get_queryset().published().search(query)

class BlogPost(models.Model): #blogpost_set -> queryset
    # id = models.IntegerField() or pk
    user = models.ForeignKey(User, default=1, null=True,on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='image/' , blank=True , null=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique= True) # hello world -> hello-world
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp =  models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now=True)

    objects = BlogPostManager() 
    class Meta:
        ordering =  [ '-publish_date' , '-updated', '-timestamp']

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    
    def get_edit_url(self):
        return f"/blog/{self.slug}/edit"
    
    def get_delete_url(self):
        return f"/blog/{self.slug}/delete"
    
