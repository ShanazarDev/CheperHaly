from django.shortcuts import render
from .models import NewsModel, NewsViewModel


def news(req):
    news_all = NewsModel.objects.all()
    if news_all:
        all_news = news_all.order_by('-pk')
        top_news = [t for t in news_all.filter(istop=True).order_by('-pk').all()[:2]]
        context = {
            'all_news': all_news,
            'top_1': top_news[0],
            'top_2': top_news[1],
        }
        return render(req, 'news/news_all.html', context)
    return render(req, 'news/news.html')


def news_one(req, title):
    news_all = NewsModel.objects.all()
    filtered_news = news_all.filter(slug_title_en=title).all()
    recent_news = news_all.order_by('-pk').exclude(slug_title_en=title).all()[:3]
    NewsViewModel.objects.update_or_create(news_post=NewsModel.objects.get(pk=[f.pk for f in filtered_news][0]),
                                           ip=req.META.get('REMOTE_ADDR'))
    context = {
        'news': filtered_news,
        'recent_news': recent_news
    }
    return render(req, 'news/news_one.html', context)
