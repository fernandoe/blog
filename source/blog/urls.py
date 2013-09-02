from django.conf.urls import patterns, url

from blog.views import BlogListView, PostTemplateView, AboutTemplateView


urlpatterns = patterns('',
    url(r'^(?P<slug>[\w\-]+)/$', PostTemplateView.as_view(), name='blog_post'),
    url(r'^$', BlogListView.as_view(), name='blog'),
    url(r'^about$', AboutTemplateView.as_view(), name='blog_about'),
    
)


