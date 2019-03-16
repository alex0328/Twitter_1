from django.shortcuts import render
from twitter.models import Tweet
from django.views import View
from django.views.generic.list import ListView

# Create your views here.

class MainPageView(ListView):
    template_name = 'twitter/index.html'
    context_object_name = 'tweets'

    def get_queryset(self):
        return Tweet.objects.all().order_by('-creation_date')