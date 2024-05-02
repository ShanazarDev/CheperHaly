from django.shortcuts import render
from .models import GalleryModel


def gallery(req):
    gallery_model = GalleryModel.objects.all()
    if gallery_model:
        images = gallery_model.order_by('-pk')
        return render(req, 'gallery/full-grid-gallery.html', {'gallery': images})
    return render(req, 'gallery/gallery.html')
