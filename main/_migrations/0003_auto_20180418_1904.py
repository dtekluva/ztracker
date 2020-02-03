# Generated by Django 2.0 on 2018-04-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180418_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='position',
        ),
        migrations.AddField(
            model_name='customer',
            name='lat',
            field=models.FloatField(blank=True, default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='lng',
            field=models.FloatField(blank=True, default=0, max_length=100),
        ),
    ]