from django.contrib import admin
from .models import NewsModel, NewsViewModel


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    model = NewsModel
    list_display = ('title', 'short_description', 'views_count', 'istop', 'image_to_admin', 'date')
    list_display_links = ['title']
    list_editable = ['views_count']

    prepopulated_fields = {'slug_title': ['title'],
                           'slug_title_ru': ['title_ru'],
                           'slug_title_en': ['title_en']}

    readonly_fields = ['image_to_admin']


# @admin.register(NewsViewModel)
# class NewsViewModelAdmin(admin.ModelAdmin):
#     model = NewsViewModel
#     list_display = ('pk', 'news_post', 'ip')

