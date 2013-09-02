from django.contrib import admin

from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    search_fields  = ["title", "published"]
    list_display   = ["created", "title", "published"]
    date_hierarchy = 'created'
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Post, PostAdmin)


class CategoryModelAdmin(admin.ModelAdmin):
    search_fields  = ["name",]
    list_display   = ["name"]
    save_on_top = True
admin.site.register(Category, CategoryModelAdmin)


