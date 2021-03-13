from django.urls import path

from apps.landing.views import PostFormView


app_name = 'landing'

urlpatterns = [
    path('home/', PostFormView.as_view(), name='index'),
]
