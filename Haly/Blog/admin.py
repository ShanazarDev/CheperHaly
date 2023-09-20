from django.contrib import admin
from .models import BlogModel, BlogViewsModel


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    model = BlogModel
    list_display = ('title', 'short_description', 'views_count', 'istop', 'image_to_admin', 'date')
    list_display_links = ['title']
    list_editable = ['views_count']

    prepopulated_fields = {'slug_title': ['title'],
                           'slug_title_ru': ['title_ru'],
                           'slug_title_en': ['title_en']}

    readonly_fields = ['image_to_admin']


@admin.register(BlogViewsModel)
class BlogViewsModelAdmin(admin.ModelAdmin):
    model = BlogViewsModel
    list_display = ('pk', 'views_ip', 'blog_foreign')