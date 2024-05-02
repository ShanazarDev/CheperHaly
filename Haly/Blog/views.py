from django.shortcuts import render
from .models import BlogModel, BlogViewsModel


def blogs(req):
    blogs_all = BlogModel.objects.all()
    if blogs_all:
        all_blogs = blogs_all.order_by('-pk')
        top_blog = [t for t in blogs_all.filter(istop=True).order_by('-pk').all()[:2]]
        context = {
            'all_blogs': all_blogs,
            'top_1': top_blog[0],
            'top_2': top_blog[1],
        }
        return render(req, 'blog/blog_all.html', context)
    return render(req, 'blog/empty-blog.html')


def blog_post(req, title):
    blogs_all = BlogModel.objects.all()
    recent_blogs = blogs_all.order_by('-pk').exclude(slug_title_en=title).all()[:3]
    blog = blogs_all.filter(slug_title_en=title).all()
    blog_pk = BlogModel.objects.get(pk=[b.pk for b in blog][0])
    BlogViewsModel.objects.update_or_create(blog_foreign=blog_pk,
                                            views_ip=req.META.get('REMOTE_ADDR'))
    context = {
        'all_blogs': recent_blogs,
        'blog': blog,
    }
    return render(req, 'blog/blog.html', context)
