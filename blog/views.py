from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from models import Post

class PostListView(ListView):
    template_name = 'home.html'
    paginate_by = 6
    queryset = Post.objects.all()
