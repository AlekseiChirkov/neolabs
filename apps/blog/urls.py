from django.urls import path

from apps.blog.views import PostAPIView

app_name = 'blog'

urlpatterns = [
    path('posts/', PostAPIView.as_view(), name='posts'),
]