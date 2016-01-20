# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20160120_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='want_cocktail',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=0, verbose_name='Je souhaite participer au cocktail'),
        ),
    ]
