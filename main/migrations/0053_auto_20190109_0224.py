# Generated by Django 2.0 on 2019-01-09 01:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0052_auto_20190109_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 9, 2, 24, 41, 798291)),
        ),
        migrations.AlterField(
            model_name='collection',
            name='stop',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 9, 2, 24, 41, 798291)),
        ),
        migrations.AlterField(
            model_name='location',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 9, 2, 24, 41, 813915)),
        ),
    ]
