from django.urls import path
from .views import blogs, blog_post

app_name = "blogs_general"

urlpatterns = [
    path("", blogs, name="blogs"),
    path("<slug:slug>", blog_post, name="blog_slug")
]
