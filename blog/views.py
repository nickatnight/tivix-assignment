from django.contrib import messages
from django.http import HttpResponseRedirect
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


def update_post_view(request, slug=None):
    """
    Update post by retrieving post object given the slug. Pre-populate
    form fields with the model instance and send neccessary context
    data to template. If the client sends post request, check if form
    is valid, save, and redirect to the instances url.

    *slug* -> Filter post search by slug
    """
    instance = get_object_or_404(Post, slug=slug)
    post_form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if post_form.is_valid():
        post_form.save()
        messages.success(request, "Post successfully updated.")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'post_form': post_form,
    }

    return render(request, 'create_post.html', context)


def create_post_view(request):
    """
    Create new post by rendering form data on post request. If form is valid,
    save the instance and redirect to post url.
    """
    post_form = PostForm(request.POST or None, request.FILES or None)

    if post_form.is_valid():
        instance = post_form.save()
        messages.success(request, "Post successfully created.")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'post_form': post_form,
    }

    return render(request, 'create_post.html', context)
