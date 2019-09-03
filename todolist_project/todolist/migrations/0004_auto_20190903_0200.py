# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20190903_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
