from django.contrib import admin
from .models import article

# Register your models here.

@admin.register(article)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'published']
    list_filter = ['published', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'published'
    ordering = ['published']