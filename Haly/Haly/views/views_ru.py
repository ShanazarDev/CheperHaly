from django.shortcuts import render
from Gallery.models import GalleryModel


def home(req):
    return render(req, 'ru/index-1.html')


def news(req):
    return render(req, 'ru/news/news_all.html')


def news_one(req):
    return render(req, 'ru/news/news_one.html')


def about_us(req):
    return render(req, 'ru/about-us.html')


def gallery(req):
    images = GalleryModel.objects.all()
    return render(req, 'ru/gallery/full-grid-gallery.html', {'gallery_ru': images})


def blog(req):
    return render(req, 'ru/blog/blog.html')
