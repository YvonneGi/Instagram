# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-18 09:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photogram', '0003_auto_20191018_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control', models.CharField(max_length=50, null=True, unique=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photogram.Post')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photogram.Post'),
        ),
    ]
