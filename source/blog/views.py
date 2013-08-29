# -*- coding:utf-8 -*-
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Post


class BlogView(ListView):
    model = Post
    template_name = "blog/blog.html"

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['EXAMPLE'] = 'EXAMPLE' 
        return context



class PostTemplateView(DetailView):
    template_name = "blog/post.html"
    model = Post

#     def get_context_data(self, **kwargs):
#         context = super(ArticleDetailView, self).get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context