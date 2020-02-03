# Generated by Django 2.0 on 2018-12-14 06:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_auto_20181214_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 14, 7, 58, 5, 806479)),
        ),
        migrations.AlterField(
            model_name='collection',
            name='stop',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 14, 7, 58, 5, 806479)),
        ),
        migrations.AlterField(
            model_name='herdsman',
            name='phone',
            field=models.IntegerField(default=' '),
        ),
        migrations.AlterField(
            model_name='incident',
            name='is_farmer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='incident',
            name='is_herdsman',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='incident',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 14, 7, 58, 5, 807976)),
        ),
    ]