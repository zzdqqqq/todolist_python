# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todomodel_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
