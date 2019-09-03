# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_remove_todomodel_created_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todomodel',
            old_name='check_box',
            new_name='completed',
        ),
    ]
