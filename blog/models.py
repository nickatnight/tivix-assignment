from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify


def upload_location(instance, filename):
    """
    Upload blog image content to the 'media' folder.
    """
    return '%s/%s/%s' % ('blog-imgs', instance.slug, filename)


class Post(models.Model):
    """
    Post model per assignment instructions.
    """
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)  # update on 1st save
    modified = models.DateTimeField(auto_now=True)  # update time stamp
                                                    # automatically upon edit
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field='width_field',
                              height_field='height_field')
    height_field = models.PositiveIntegerField(default='300')
    width_field = models.PositiveIntegerField(default='300')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('t-blog:post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Post Entry"
        verbose_name_plural = "Post Entries"
        ordering = ["-created"]
