# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='heading_image',
            field=models.ImageField(default='', max_length=200, upload_to='blog/'),
        ),
    ]