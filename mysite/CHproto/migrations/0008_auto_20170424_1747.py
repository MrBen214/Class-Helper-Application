# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CHproto', '0007_auto_20170424_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='month_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id_num',
            field=models.IntegerField(unique=True),
        ),
    ]
