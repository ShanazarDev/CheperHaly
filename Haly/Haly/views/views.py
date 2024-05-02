import django.http
from django.shortcuts import render
from Gallery.models import GalleryHomeModel
from Blog.models import BlogModel


def home(req: django.http.HttpRequest):
    blog = BlogModel.objects.all()
    gallery = GalleryHomeModel.objects.all()
    if blog:
        gallery_big_carpet = gallery.filter(category='tabs-2-1').all()[:3]
        gallery_products = gallery.filter(category='tabs-2-2').all()[:3]
        gallery_accessories = gallery.filter(category='tabs-2-3').all()[:3]
        blogs_home = blog.order_by('-pk').all()[:3]
        print(req.path_info, req.get_full_path_info())
        return render(req, 'index-1.html',
                      {
                          'blog_home': blogs_home,
                          'gallery_big_carpet': gallery_big_carpet,
                          'gallery_products': gallery_products,
                          'gallery_accessories': gallery_accessories
                      }
                      )
    return render(req, 'index-1.html', {'gallery_home': gallery})


def about_us(req):
    return render(req, 'about-us.html')
