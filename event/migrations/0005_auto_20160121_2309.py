# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20160121_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created',
            field=models.DateTimeField(verbose_name='Created', default=datetime.datetime(2016, 1, 21, 22, 9, 37, 567740, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='hits',
            field=models.PositiveIntegerField(verbose_name='Hits', default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='modified',
            field=models.DateTimeField(verbose_name='Modified', default=datetime.datetime(2016, 1, 21, 22, 9, 45, 584164, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
