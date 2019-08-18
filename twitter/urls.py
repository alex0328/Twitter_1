from django.urls import path
from django.urls import include
from django.views import generic
from twitter.views import MainPageView
from twitter import views

app_name = 'twitter'
urlpatterns = [
    path('', MainPageView.as_view(template_name='twitter/index.html'),
         name='index'),
    path('register', views.RegisterView.as_view(),name='register'),
    path('compose/', views.ComposeView.as_view(), name='compose'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('user/<int:pk>/', views.AuthorDetailView.as_view(),name='author-detail'),
    path('tweet/<int:pk>/', views.TweetDetailView.as_view(), name='tweet-detail')
]