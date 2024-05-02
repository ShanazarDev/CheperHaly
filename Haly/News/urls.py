from django.urls import path
from .views import news, news_one

app_name = "news_general"

urlpatterns = [
    path('', news, name="news_all"),
    path('<slug:slug>', news_one, name="news_slug")
]
