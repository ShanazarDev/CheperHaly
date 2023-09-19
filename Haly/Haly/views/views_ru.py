from django.shortcuts import render
from Gallery.models import GalleryModel
from News.models import NewsModel


def home(req):
    return render(req, 'ru/index-1.html')


def news(req):
    all_news = NewsModel.objects.all()
    top_news = [t for t in NewsModel.objects.filter(istop=True).all()[:2]]
    context = {
        'all_news': all_news,
        'top_news': top_news
    }
    return render(req, 'ru/news/news_all.html', context)


def news_one(req, title):
    filtered_news = NewsModel.objects.filter(slug_title_ru=title).all()
    recent_news = NewsModel.objects.all().order_by('-pk')[:2]
    context = {
        'news': filtered_news,
        'recent_news': recent_news
    }
    return render(req, 'ru/news/news_one.html', context)


def about_us(req):
    return render(req, 'ru/about-us.html')


def gallery(req):
    images = GalleryModel.objects.all()
    return render(req, 'ru/gallery/full-grid-gallery.html', {'gallery_ru': images})


def blog(req):
    return render(req, 'ru/blog/blog.html')
