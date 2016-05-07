from django.conf.urls import url

from .views import (
    create_post_view,
    update_post_view,
    BlogDetailView,
    PostListView,
)

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='home'),
    url(r'^create-post/', create_post_view, name='create_post'),
    url(r'^(?P<slug>\S+)/update/$', update_post_view,
        name='update_post'),
    url(r'^(?P<slug>\S+)/$', BlogDetailView.as_view(), name='post_detail'),
]
