# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-21 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='产品图片'),
        ),
    ]
