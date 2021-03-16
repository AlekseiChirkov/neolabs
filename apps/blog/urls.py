from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'blog'

router = routers.DefaultRouter()
router.register('post', views.PostViewSet)
router.register('category', views.PostCategoryViewSet)
router.register('author', views.AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]