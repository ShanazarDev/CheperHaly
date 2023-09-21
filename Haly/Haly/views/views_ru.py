from django.shortcuts import render
from Gallery.models import GalleryModel, GalleryHomeModel, HomeBackgroundModel
from News.models import NewsModel, NewsViewModel
from Blog.models import BlogModel, BlogViewsModel


def home(req):
    if BlogModel.objects.all() is not None:
        gallery_big_carpet = GalleryHomeModel.objects.filter(category='tabs-2-1').all()[:3]
        gallery_products = GalleryHomeModel.objects.filter(category='tabs-2-2').all()[:3]
        gallery_accessories = GalleryHomeModel.objects.filter(category='tabs-2-3').all()[:3]
        background = HomeBackgroundModel.objects.last()
        blogs_home = BlogModel.objects.order_by('-pk').all()[:3]
        return render(req, 'ru/index-1.html',
                      {
                          'background': background,
                          'blog_home': blogs_home,
                          'gallery_big_carpet': gallery_big_carpet,
                          'gallery_products': gallery_products,
                          'gallery_accessories': gallery_accessories
                      }
                      )
    gallery_home = GalleryHomeModel.objects.all()
    return render(req, 'ru/index-1.html', {'gallery_home': gallery_home})


def about_us(req):
    background = HomeBackgroundModel.objects.last()
    return render(req, 'ru/about-us.html', {'background': background})


def gallery(req):
    if GalleryModel.objects.all() is not None:
        images = GalleryModel.objects.order_by('-pk')
        background = HomeBackgroundModel.objects.last()
        return render(req, 'ru/gallery/full-grid-gallery.html',
                      {'gallery_ru': images, 'background': background})
    return render(req, 'ru/gallery/gallery.html')


def news(req):
    if NewsModel.objects.all() is not None:
        all_news = NewsModel.objects.order_by('-pk')
        top_news = [t for t in NewsModel.objects.filter(istop=True).order_by('-pk').all()[:2]]
        background = HomeBackgroundModel.objects.last()
        context = {
            'all_news': all_news,
            'top_news': top_news,
            'background': background
        }
        return render(req, 'ru/news/news_all.html', context)
    return render(req, 'ru/news/news.html')


def news_one(req, title):
    filtered_news = NewsModel.objects.filter(slug_title_ru=title).all()
    recent_news = NewsModel.objects.order_by('-pk').exclude(slug_title_ru=title).all()[:3]
    NewsViewModel.objects.update_or_create(news_post=NewsModel.objects.get(pk=[f.pk for f in filtered_news][0]),
                                           ip=req.META.get('REMOTE_ADDR'))
    context = {
        'news': filtered_news,
        'recent_news': recent_news
    }
    return render(req, 'ru/news/news_one.html', context)


def blogs(req):
    if BlogModel.objects.all() is not None:
        all_blogs = BlogModel.objects.order_by('-pk')
        top_blog = [t for t in BlogModel.objects.filter(istop=True).order_by('-pk').all()[:2]]
        background = HomeBackgroundModel.objects.last()
        context = {
            'all_blogs': all_blogs,
            'top_blog': top_blog,
            'background': background
        }
        return render(req, 'ru/blog/blog_all.html', context)
    return render(req, 'ru/blog/empty-blog.html')


def blog_post(req, title):
    all_blogs = BlogModel.objects.order_by('-pk').exclude(slug_title_ru=title).all()[:3]
    blog = BlogModel.objects.filter(slug_title_ru=title).all()
    blog_pk = BlogModel.objects.get(pk=[b.pk for b in blog][0])
    BlogViewsModel.objects.update_or_create(blog_foreign=blog_pk,
                                            views_ip=req.META.get('REMOTE_ADDR'))

    context = {
        'all_blogs': all_blogs,
        'blog': blog,
    }
    return render(req, 'ru/blog/blog.html', context)
