from django.contrib import admin
from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name', 'slug']
    search_fields = ['id', 'name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'author', 'created_on']
    list_display_links = ['id', 'title', 'slug']
    search_fields = ['id', 'title']
    list_filter = ['author']
    filter_horizontal = ['categories']
