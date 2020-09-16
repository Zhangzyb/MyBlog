from django.urls import path
from . import views


app_name = 'comment'
urlpatterns = [
    path('<slug:english_name>/comments/', views.comment, name='comment'),
    path('<slug:english_name>/comments/<int:comment_id>/<int:reply_id>/', views.sub_comment, name='sub_comment'),
]