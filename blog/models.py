from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200, default=True)
    created = models.DateTimeField(auto_now_add=True)  # update on 1st save
    modified = models.DateTimeField(auto_now=True)  # update time stamp
                                                    # automatically upon save

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Post Entry"
        verbose_name_plural = "Post Entries"
        ordering = ["-created"]
