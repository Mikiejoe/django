from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Post

class PostList(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'posts'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = {'title','body'}
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')