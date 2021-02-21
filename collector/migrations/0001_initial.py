# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlipSubmit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('full_name', models.CharField(max_length=120, null=True, blank=True)),
                ('language_involved', models.CharField(max_length=120)),
                ('where', models.CharField(max_length=120, null=True, blank=True)),
                ('topic', models.CharField(max_length=120, null=True, blank=True)),
                ('intended_sentence', models.CharField(max_length=120)),
                ('perceived_sentence', models.CharField(max_length=120)),
                ('speaker_info', models.CharField(max_length=120)),
                ('hearer_info', models.CharField(max_length=120)),
                ('realise_how', models.CharField(max_length=120)),
                ('other_info', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
