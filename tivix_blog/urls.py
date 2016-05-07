from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


# Give blog a namespace for portabilty
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include("blog.urls", namespace='t-blog')),
]

# Only serve static files from same workstation in dev mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
