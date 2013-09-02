# -*- coding:utf-8 -*-
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Post


class BlogListView(ListView):
    model = Post
    template_name = "blog/blog.html"

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['menu'] = 'blog' 
        return context

    def get_queryset(self):
        return Post.objects.filter(published=True)


class PostTemplateView(DetailView):
    template_name = "blog/post.html"
    model = Post


class AboutTemplateView(TemplateView):
    template_name = "blog/about.html"
    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data(**kwargs)
        context['menu'] = 'about' 
        return context


