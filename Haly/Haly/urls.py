"""
URL configuration for Haly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from .views import (views_ru, views_en, views_tm)
from django.conf.urls.static import static
from django.conf import settings
from .settings import DEBUG
from Haly.sitemap import *
from News.feeds import NewsRSS


urlpatterns_ru = [
    path('', views_ru.home, name='home_ru'),
    path('news/', views_ru.news, name='news_ru'),
    path(r'news/<title>', views_ru.news_one, name='news_ru_one'),
    path('about-us/', views_ru.about_us, name='about_us_ru'),
    path('gallery/', views_ru.gallery, name='gallery_ru'),
    path('blogs/', views_ru.blogs, name='blog_ru'),
    path('blog/post/<title>', views_ru.blog_post, name='blog_ru_post')
]

urlpatterns_en = [
    path('', views_en.home, name='home_en'),
    path('news/', views_en.news, name='news_en'),
    path(r'news/<title>', views_en.news_one, name='news_en_one'),
    path('about-us/', views_en.about_us, name='about_us_en'),
    path('gallery/', views_en.gallery, name='gallery_en'),
    path('blogs/', views_en.blogs, name='blog_en'),
    path('blog/post/<title>', views_en.blog_post, name='blog_en_post')
]

sitemaps = {
    'static': StaticSiteMap,
    'news': NewsSiteMap,
    'blog': BlogSiteMap,
    'always': AlwaysSitemap
    }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ru/', include(urlpatterns_ru)),
    path('en/', include(urlpatterns_en)),
    path('', views_tm.home, name='home'),
    path('news/', views_tm.news, name='news'),
    path(r'news/<title>', views_tm.news_one, name='news_one'),
    path('about-us/', views_tm.about_us, name='about_us'),
    path('gallery/', views_tm.gallery, name='gallery'),
    path('blogs/', views_tm.blogs, name='blog'),
    path('blog/post/<title>', views_tm.blog_post, name='blog_post'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('rss/', NewsRSS())
]

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Ceper Haly Muzei'
admin.site.site_title = 'Ceper Haly Muzei'
