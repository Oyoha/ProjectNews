from django.views.generic import ListView, DetailView
from .models import *


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-public_time')


class NewDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'post'

