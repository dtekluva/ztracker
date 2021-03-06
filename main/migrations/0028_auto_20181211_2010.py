# Generated by Django 2.0 on 2018-12-11 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20181211_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 11, 20, 10, 42, 657129)),
        ),
        migrations.AlterField(
            model_name='collection',
            name='stop',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 11, 20, 10, 42, 657129)),
        ),
        migrations.AlterField(
            model_name='farmland',
            name='db_id',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='herdsman',
            name='db_id',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 11, 20, 10, 42, 659126)),
        ),
    ]
