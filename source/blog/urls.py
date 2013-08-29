from django.conf.urls import patterns, url

from blog.views import BlogView, PostTemplateView


urlpatterns = patterns('',
    url(r'^(?P<slug>[\w\-]+)/$', PostTemplateView.as_view(), name='blog_post'),
    url(r'^$', BlogView.as_view(), name='blog'),
)


