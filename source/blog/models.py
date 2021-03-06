from django.core.urlresolvers import reverse
from django.db import models
from django_extensions.db.fields import UUIDField


class Category(models.Model):
    uuid      = UUIDField(primary_key=True)
    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)
    name      = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ['name']



class Post(models.Model):
    uuid       = UUIDField(primary_key=True)
    created    = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True)
    title      = models.CharField(max_length=255)
    slug       = models.SlugField(unique=True, max_length=255)
    content    = models.TextField()
    published  = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('blog_post', args=[self.slug])

    class Meta:
        ordering = ['-created']

