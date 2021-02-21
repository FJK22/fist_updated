# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0002_auto_20170112_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slipsubmit',
            name='email',
            field=models.EmailField(verbose_name='Email address (Optional)', max_length=254, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='full_name',
            field=models.CharField(verbose_name="Your Full Name (Reporter's name) (Optional)", max_length=120, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='hearer_info',
            field=models.CharField(verbose_name="Hearer's information: Sex, Age, Origin, Languages known (and their fluency)", max_length=120),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='intended_sentence',
            field=models.CharField(verbose_name='Intended sentence', max_length=120),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='language_involved',
            field=models.CharField(verbose_name='Language(s) Involved', max_length=120),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='other_info',
            field=models.CharField(verbose_name='Other information: Anything from.: Noise level, Speakers or Hearers have any particular accents, tiredness, echoy room...', max_length=120),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='perceived_sentence',
            field=models.CharField(verbose_name='Perceived sentence', max_length=120),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='realise_how',
            field=models.CharField(verbose_name='How did you realise the mishearing?', max_length=120),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='speaker_info',
            field=models.CharField(verbose_name="Speaker's information: Sex, Age, Origin, Languages known (and their fluency)", max_length=120),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='topic',
            field=models.CharField(verbose_name='Nature/Topic of conversation (e.g. about homework, shopping, talking over the phone.)', max_length=120, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='slipsubmit',
            name='where',
            field=models.CharField(verbose_name='Where did it happen?', max_length=120, blank=True, null=True),
        ),
    ]
