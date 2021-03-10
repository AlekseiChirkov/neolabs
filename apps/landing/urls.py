from django.urls import path

from apps.landing.views import IndexPageView


app_name = 'landing'

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
]
