from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from News.models import NewsModel
from Blog.models import BlogModel


class AlwaysSitemap(Sitemap):
    changefreq = 'always'
    priority = 1

    def items(self):
        return ['news', 'gallery', 'blog']

    def location(self, item):
        return reverse(item)


class StaticSiteMap(Sitemap):
    changefreq = 'never'
    priority = 1

    def items(self):
        return ['home', 'about_us']

    def location(self, item):
        return reverse(item)


class BlogSiteMap(Sitemap):
    def lastmod(self, obj):
        return obj.date

    def items(self):
        return BlogModel.objects.all()


class NewsSiteMap(Sitemap):
    def lastmod(self, obj):
        return obj.date

    def items(self):
        return NewsModel.objects.all()
