from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'owner')
    list_filter = ('title', 'is_published', 'owner')
    search_fields = ('content', 'title')
