# -*- coding:utf-8 -*-
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
import markdown


register = template.Library()


@register.filter(name='markdown')
def blog_markdown(text):
    html = markdown.markdown(text)
    if settings.DEBUG:
        print "=" * 100
        print html
        print "=" * 100
    return mark_safe(html)


# import markdown
# 
# from django import template
# from django.template.defaultfilters import stringfilter
# from django.utils.encoding import force_unicode
# from django.utils.safestring import mark_safe
# 
# register = template.Library()
# 
# @register.filter(is_safe=True)
# @stringfilter
# def my_markdown(value):
#     extensions = ["nl2br", ]
# 
#     return mark_safe(markdown.markdown(force_unicode(value),
#                                        extensions,
#                                        safe_mode=True,
#                                        enable_attributes=False))