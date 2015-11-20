# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, default=uuid.uuid4)),
                ('color', models.CharField(choices=[(1, 'white'), (2, 'black'), (3, 'grey'), (4, 'red')], max_length=15)),
                ('year', models.PositiveSmallIntegerField()),
                ('model', models.CharField(choices=[(1, 'kia'), (2, 'subaru'), (3, 'audi'), (4, 'alfa romeo')], max_length=15)),
                ('cc', models.PositiveSmallIntegerField()),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
    ]
