from django.contrib import admin
from .models import NewsModel, NewsViewModel
from modeltranslation.admin import TranslationAdmin


@admin.register(NewsModel)
class NewsAdmin(TranslationAdmin):
    exclude = ('date',)
    list_display = ('title', 'short_description', 'views_count', 'istop', 'image_to_admin', 'date')
    readonly_fields = ['image_to_admin']
    prepopulated_fields = {'slug_title': ['title']}


@admin.register(NewsViewModel)
class NewsViewModelAdmin(admin.ModelAdmin):
    model = NewsViewModel
    list_display = ('pk', 'news_post', 'ip')
