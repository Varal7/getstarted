# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import event.models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_auto_20160206_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='cv',
            field=models.FileField(verbose_name='Ton CV au format .pdf (facultatif) :', blank=True, upload_to=event.models.Participant.user_directory_path),
        ),
    ]
