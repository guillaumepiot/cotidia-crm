# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 09:29
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20160330_1209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]