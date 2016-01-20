# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import event.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], max_length=254, unique=True, error_messages={'unique': 'Tu es déjà inscrit'}, help_text='Required. 254 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name="Nom d'utilisateur")),
                ('first_name', models.CharField(verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30)),
                ('email', models.EmailField(unique=True, error_messages={'unique': 'Un autre utilisateur a déjà cette adresse de courriel.'}, verbose_name='email address', max_length=254)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('last_visit', models.DateField(auto_now=True)),
                ('promo', models.CharField(verbose_name='Promotion', max_length=30)),
                ('found_stage', models.BooleanField(default=1, verbose_name='As-tu trouvé ton prochain stage ?', choices=[(True, 'Yes'), (False, 'No')])),
                ('year_in_school', models.CharField(default=2, verbose_name="Ton niveau d'études", choices=[('2', '2A'), ('3', '3A'), ('M', 'Master'), ('D', 'Doctorat')], max_length=2)),
                ('domains', models.TextField(verbose_name="Quels domaines t'intéresseraient ?", blank=True)),
                ('missions', models.TextField(verbose_name='Quels types de missions souhaiterais tu mener en stage ?', blank=True)),
                ('cv', models.FileField(upload_to=event.models.Participant.user_directory_path, verbose_name='Ton CV :')),
            ],
        ),
    ]
