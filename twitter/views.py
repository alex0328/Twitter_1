from django.shortcuts import render, redirect
from twitter.models import Tweet
from django.views import View
from django.views.generic.list import ListView
from twitter import forms
from twitter import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy



# Create your views here.

class MainPageView(ListView):
    template_name = 'twitter/index.html'
    context_object_name = 'tweets'

    def get_queryset(self):
        return Tweet.objects.all().order_by('-creation_date')


class RegisterView(View):
    form_class = forms.UserRegisterForm
    template_name = 'twitter/register.html'

    def get(self, request):
        return render(request, 'twitter/register.html',
                      {'form': forms.UserRegisterForm()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            return redirect('/')

        return render(request, self.template_name, {'form': form})

class ComposeView(LoginRequiredMixin, CreateView):
    model = models.Tweet
    form_class = forms.TweetForm
    success_url = reverse_lazy('twitter:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        tweets = models.Tweet.objects.filter(
            author=request.user).order_by('-creation_date')
        return render(request, 'twitter/profile.html', {'tweets': tweets})

class AuthorDetailView(View):
    def get(self, request, pk):
        tweets = Tweet.objects.filter(author=pk).order_by('-creation_date')
        return render(request, 'twitter/user_tweet.html', {'tweets': tweets})

class TweetDetailView(View):
    model = models.Tweet

class DetailView(View):
    pass