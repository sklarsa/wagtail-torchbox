# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-26 10:23
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0049_auto_20160819_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='intro_body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
