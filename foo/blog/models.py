from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    content = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['published_on', ]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def get_absolute_url(self):
        args = [self.slug]
        return reverse('blog:display_post', args=args)
