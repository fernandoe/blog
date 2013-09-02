# -*- coding:utf-8 -*-
from blog.models import Post
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView



class BlogView(ListView):
    model = Post
    template_name = "blog/blog.html"

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['menu'] = 'blog' 
        return context


class PostTemplateView(DetailView):
    template_name = "blog/post.html"
    model = Post


class AboutTemplateView(TemplateView):
    template_name = "blog/about.html"
    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data(**kwargs)
        context['menu'] = 'about' 
        return context


