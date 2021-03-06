# Generated by Django 2.0 on 2019-06-02 01:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0055_auto_20190213_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lng', models.FloatField(blank=True, default=0, max_length=100)),
                ('lat', models.FloatField(blank=True, default=0, max_length=100)),
                ('speed', models.FloatField(blank=True, default=0, max_length=100)),
                ('accuracy', models.FloatField(blank=True, default=0, max_length=100)),
                ('location', models.TextField(blank=True, default='', null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('details', models.TextField(blank=True, default='', max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_farmer', models.BooleanField(default=False)),
                ('is_herdsman', models.BooleanField(default=False)),
                ('is_resolved', models.BooleanField(default=False)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Incident')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.AlterField(
            model_name='collection',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 2, 2, 46, 15, 728812)),
        ),
        migrations.AlterField(
            model_name='collection',
            name='stop',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 2, 2, 46, 15, 728812)),
        ),
        migrations.AlterField(
            model_name='location',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 2, 2, 46, 15, 730812)),
        ),
    ]
