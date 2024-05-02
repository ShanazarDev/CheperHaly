from django.contrib.syndication.views import Feed, feedgenerator
from django.urls import reverse
from .models import NewsModel
from django.core.files.storage.base import Storage


class CustomRss201rev2Feed(feedgenerator.Rss201rev2Feed):
    content_type = 'text/xml; charset=utf-8'

    def rss_attributes(self):
        attrs = super().rss_attributes()
        attrs['xmlns:content'] = 'http://purl.org/rss/1.0/modules/content/'
        attrs['xmlns:media'] = 'http://search.yahoo.com/mrss/'
        attrs['xmlns:wfw'] = 'http://wellformedweb.org/CommentAPI/'
        return attrs


class NewsRSS(Feed):
    title = "CeperHaly"
    link = "/news/"
    description = "Tazelikler"
    language = "tk"

    feed_type = CustomRss201rev2Feed

    def items(self):
        return NewsModel.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_pubdate(self, item):
        return item.date

    def item_guid(self, item):
        return item.slug_title

    def get_object(self, request, *args, **kwargs):
        self.request = request
        return super(NewsRSS, self).get_object(request, *args, **kwargs)

    def get_image_url(self, url):
        return self.request.build_absolute_uri('{}'.format(url))

    def item_enclosures(self, item):
        return [feedgenerator.Enclosure(self.get_image_url(item.image.url), str(item.image.size),
                                        'image/{}'.format(item.image.name.split('.')[-1]))]

    def item_link(self, item):
        return reverse("news_general:news_slug", args=[item.slug_title])
