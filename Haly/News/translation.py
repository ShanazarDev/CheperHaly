from modeltranslation.translator import register, TranslationOptions
from .models import NewsModel


@register(NewsModel)
class NewsTranslation(TranslationOptions):
    fields = ("title", "short_description", "text", "slug_title")
