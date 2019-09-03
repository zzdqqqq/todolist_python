# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 3, 1, 50, 40, 590053, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
