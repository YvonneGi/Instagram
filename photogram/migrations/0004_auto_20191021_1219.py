# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-21 10:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photogram', '0003_auto_20191020_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photogram.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
