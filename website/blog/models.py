from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

#how to get users: from django.contrib.auth import get_user_model
# j = User.onjects.first : (first user)
# to take all BlogPosts: j.blogpost_set.all()

class BlogPost(models.Model): #blogpost_set -> queryset
    # id = models.IntegerField() or pk
    user = models.ForeignKey(User, default=1, null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique= True) # hello world -> hello-world
    content = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    
    def get_edit_url(self):
        return f"/blog/{self.slug}/edit"
    
    def get_delete_url(self):
        return f"/blog/{self.slug}/delete"
    
