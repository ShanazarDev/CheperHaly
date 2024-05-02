from django.urls import path
from .views import gallery

app_name = "gallery_general"

urlpatterns = [
    path('', gallery, name="gallery"),
]
