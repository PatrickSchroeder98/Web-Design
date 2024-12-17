from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, CreateView)
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))


class PostDetailView(DetailView):
    model = Post


class CreatePostView(CreateView):

    model = Post
