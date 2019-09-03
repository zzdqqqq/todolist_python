# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20190903_0200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todomodel',
            name='created_time',
        ),
    ]
