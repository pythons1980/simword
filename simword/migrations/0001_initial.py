# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StringList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('string_list', picklefield.fields.PickledObjectField(editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at', db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated at', db_index=True)),
            ],
        ),
    ]
