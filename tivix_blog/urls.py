from django.conf.urls import include, url
from django.contrib import admin


# Give blog a namespace for portabilty
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include("blog.urls", namespace='t-blog')),
]
