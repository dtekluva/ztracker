# Generated by Django 2.0 on 2018-12-13 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20181213_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 13, 14, 35, 19, 944419)),
        ),
        migrations.AlterField(
            model_name='collection',
            name='stop',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 13, 14, 35, 19, 944419)),
        ),
        migrations.AlterField(
            model_name='farmland',
            name='details',
            field=models.TextField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='herdsman',
            name='details',
            field=models.TextField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 13, 14, 35, 19, 946421)),
        ),
    ]