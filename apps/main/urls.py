from django.urls import path
from apps.main.views import index, articles

urlpatterns = [
    path('', index, name='index'),
    path('articles', articles, name='articles')
]