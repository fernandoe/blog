from blog.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    search_fields  = ["title", "published"]
    list_display   = ["created", "title", "published"]
    date_hierarchy = 'created'
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Post, PostAdmin)


