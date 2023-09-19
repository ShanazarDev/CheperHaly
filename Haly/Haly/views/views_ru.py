from django.shortcuts import render
from Gallery.models import GalleryModel
from News.models import NewsModel


def home(req):
    return render(req, 'ru/index-1.html')


def news(req):
    return render(req, 'ru/news/news_all.html')


def news_one(req):
    news = NewsModel.objects.all()
    return render(req, 'ru/news/news_one.html', {'news': news})


def about_us(req):
    return render(req, 'ru/about-us.html')


def gallery(req):
    images = GalleryModel.objects.all()
    return render(req, 'ru/gallery/full-grid-gallery.html', {'gallery_ru': images})


def blog(req):
    return render(req, 'ru/blog/blog.html')
