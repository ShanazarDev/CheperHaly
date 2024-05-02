from modeltranslation.translator import register, TranslationOptions
from .models import BlogModel


@register(BlogModel)
class NewsTranslation(TranslationOptions):
    fields = ("title", "short_description", "text", "slug_title")
