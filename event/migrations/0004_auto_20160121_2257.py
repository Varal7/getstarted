# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_participant_want_cocktail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(default='Get Started', verbose_name="Nom de l'événement", max_length=254)),
                ('is_active', models.BooleanField(default=False, verbose_name='active', help_text='Activer pour lancer les inscriptions')),
            ],
        ),
        migrations.AlterField(
            model_name='participant',
            name='want_cocktail',
            field=models.BooleanField(default=0, choices=[(True, 'Yes'), (False, 'No')], verbose_name='Souhaites-tu participer au cocktail ?'),
        ),
    ]
