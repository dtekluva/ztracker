# Generated by Django 2.0 on 2018-11-27 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181126_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='herdsman',
            name='state',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='location',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 27, 8, 43, 12, 948681)),
        ),
    ]
