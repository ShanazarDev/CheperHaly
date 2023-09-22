from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from News.models import NewsModel
from Blog.models import BlogModel


class StaticViewSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.8

    def items(self):
        return ['home', 'news', 'gallery', 'blog', 'about_us']

    def location(self, item):
        return reverse(item)


class BlogSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def lastmod(self, obj):
        return obj.date

    def items(self):
        return BlogModel.objects.all()


class NewsSiteMap(Sitemap):
    changefreq = 'always'
    priority = 1

    def lastmod(self, obj):
        return obj.date

    def items(self):
        return NewsModel.objects.all()
