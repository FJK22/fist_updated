# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slipsubmit',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name=b'Email address (Optional)', blank=True),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='full_name',
            field=models.CharField(max_length=120, null=True, verbose_name=b"Your Full Name (Reporter's name) (Optional)", blank=True),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='hearer_info',
            field=models.CharField(max_length=120, verbose_name=b"Hearer's information: Sex, Age, Origin, Languages known (and their fluency)"),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='intended_sentence',
            field=models.CharField(max_length=120, verbose_name=b'Intended sentence'),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='language_involved',
            field=models.CharField(max_length=120, verbose_name=b'Language(s) Involved'),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='other_info',
            field=models.CharField(max_length=120, verbose_name=b'Other information: Anything from.: Noise level, Speakers or Hearers have any particular accents, tiredness, echoy room...'),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='perceived_sentence',
            field=models.CharField(max_length=120, verbose_name=b'Perceived sentence'),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='realise_how',
            field=models.CharField(max_length=120, verbose_name=b'How did you realise the mishearing?'),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='speaker_info',
            field=models.CharField(max_length=120, verbose_name=b"Speaker's information: Sex, Age, Origin, Languages known (and their fluency)"),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='topic',
            field=models.CharField(max_length=120, null=True, verbose_name=b'Nature/Topic of conversation (e.g. about homework, shopping, talking over the phone.)', blank=True),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='where',
            field=models.CharField(max_length=120, null=True, verbose_name=b'Where did it happen?', blank=True),
        ),
    ]
