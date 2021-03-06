# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-17 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0027_homepageclients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='intro',
            new_name='hero_intro',
        ),
        migrations.AddField(
            model_name='homepage',
            name='blog_title',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='clients_title',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_body',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_title',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='work_title',
            field=models.TextField(blank=True),
        ),
    ]
