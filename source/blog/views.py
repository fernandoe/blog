# -*- coding:utf-8 -*-
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Post, Category


class BlogListView(ListView):
    model = Post
    template_name = "blog/blog.html"

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['menu'] = 'blog' 
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        posts = Post.objects.filter(published=True)
        category = self.request.GET.get('category', None)
        if category:
            category = Category.objects.get(name=category)
            posts = posts.filter(categories__name=category)
        return posts


class PostTemplateView(DetailView):
    template_name = "blog/post.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostTemplateView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['menu'] = None
        return context


class AboutTemplateView(TemplateView):
    template_name = "blog/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data(**kwargs)
        context['menu'] = 'about' 
        return context


