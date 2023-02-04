from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.
# class HomePageView(TemplateView):
#     template_name='home.html'
class HomePageViews(ListView):
    model=Post
    template_name='homes.html'
class DetailPageViews(DetailView):
    model=Post
    template_name='post_detail.html'
class BlogCreateViews(CreateView):
    model=Post
    template_name='blog_create.html'
    fields=['title', 'author', 'body',]
class BlogUpdateViews(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title', 'body']
class BlogDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('homes')
class AboutPageViews(ListView):
    model=Post
    template_name='about.html'

