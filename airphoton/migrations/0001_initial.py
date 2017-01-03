# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airphoton.Team'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='team',
            field=models.ManyToManyField(blank=True, null=True, to='airphoton.Team'),
        ),
    ]
