# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 07:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160721_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='auth_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]