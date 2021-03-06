from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<slug:english_name>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('tags/<slug:name>/', views.tag, name='tag'),
    path('category/<slug:cate_name>/', views.category, name='category'),
    path('article/inc_like/<slug:english_name>/', views.add_likes, name='likes'),
]