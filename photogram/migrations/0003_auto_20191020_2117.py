# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-20 19:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogram', '0002_remove_profile_phonenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='profile',
            new_name='upload_by',
        ),
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
    ]