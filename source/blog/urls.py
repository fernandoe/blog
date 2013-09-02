from blog.views import BlogView, PostTemplateView, AboutTemplateView
from django.conf.urls import patterns, url



urlpatterns = patterns('',
    url(r'^(?P<slug>[\w\-]+)/$', PostTemplateView.as_view(), name='blog_post'),
    url(r'^$', BlogView.as_view(), name='blog'),
    url(r'^about$', AboutTemplateView.as_view(), name='blog_about'),
    
)


