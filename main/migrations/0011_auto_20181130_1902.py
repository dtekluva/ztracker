# Generated by Django 2.0 on 2018-11-30 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20181130_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 30, 19, 2, 23, 302057)),
        ),
    ]
