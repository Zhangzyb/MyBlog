from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:pk>/', views.detail, name='detail'),
]