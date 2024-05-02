from modeltranslation.translator import register, TranslationOptions
from .models import GalleryModel, GalleryHomeModel


@register(GalleryModel)
class GalleryTranslation(TranslationOptions):
    fields = ("name", "description")


@register(GalleryHomeModel)
class GalleryHomeTranslation(TranslationOptions):
    fields = ("name", "description")
