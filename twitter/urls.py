from django.urls import path

from django.views import generic
from twitter.views import MainPageView

app_name = 'twitter'
urlpatterns = [
    path('', MainPageView.as_view(template_name='twitter/index.html'),
         name='index'),
]