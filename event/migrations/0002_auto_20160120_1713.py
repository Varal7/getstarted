# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import event.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='cv',
            field=models.FileField(upload_to=event.models.Participant.user_directory_path, verbose_name='Ton CV (format .pdf) :'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.EmailField(error_messages={}, verbose_name='email address', max_length=254),
        ),
        migrations.AlterField(
            model_name='participant',
            name='username',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], help_text='Required. 254 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=254, verbose_name="Nom d'utilisateur", error_messages={}),
        ),
    ]
