from django.contrib import admin
from .models import GalleryModel


@admin.register(GalleryModel)
class GalleryAdmin(admin.ModelAdmin):
    model = GalleryModel
    list_display = ('image_to_admin', 'name', 'description', 'size_of_carpet', 'category')
    list_display_links = ['name']
    readonly_fields = ['image_to_admin']

