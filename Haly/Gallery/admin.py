from django.contrib import admin
from .models import GalleryModel, GalleryHomeModel, HomeBackgroundModel


@admin.register(GalleryModel)
class GalleryAdmin(admin.ModelAdmin):
    model = GalleryModel
    list_display = ('image_to_admin', 'name', 'description', 'size_of_carpet', 'category')
    list_display_links = ['name']
    readonly_fields = ['image_to_admin']


@admin.register(GalleryHomeModel)
class GalleryHomeModelAdmin(admin.ModelAdmin):
    model = GalleryHomeModel
    list_display = ('name', 'description', 'size_of_carpet', 'category')
    list_display_links = ['name']


@admin.register(HomeBackgroundModel)
class HomeBackgroundModelAdmin(admin.ModelAdmin):
    model = HomeBackgroundModel
    list_display = ('image_to_admin', 'date')
    readonly_fields = ['image_to_admin']
