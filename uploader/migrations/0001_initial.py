# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='f/', verbose_name='Upload a File')),
                ('expireDate', models.DateTimeField(verbose_name='expiration time')),
            ],
        ),
    ]
