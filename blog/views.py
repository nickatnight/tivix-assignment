from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView


class PostListView(ListView):
    template_name = 'home.html'
    paginate_by = 10
