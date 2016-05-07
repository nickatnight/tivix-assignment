# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='height_field',
            field=models.PositiveIntegerField(default=b'300'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=blog.models.upload_location, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='width_field',
            field=models.PositiveIntegerField(default=b'300'),
        ),
    ]
