# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='texto_html',
            field=models.TextField(null=True, editable=False, blank=True),
        ),
    ]
