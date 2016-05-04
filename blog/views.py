from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .forms import PostForm
from .models import Post


class PostListView(ListView):
    template_name = 'home.html'
    paginate_by = 6
    queryset = Post.objects.all()


class BlogDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post


def create_post_view(request):
    post_form = PostForm(request.POST)

    if post_form.is_valid():
        print post_form['body']
        post_form.save()

    context = {
        "post_form": post_form,
    }
    return render(request, 'create_post.html', context)
