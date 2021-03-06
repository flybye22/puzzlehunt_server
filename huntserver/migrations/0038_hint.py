# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-07 19:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('huntserver', '0037_auto_20190925_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(help_text=b'The text of the request for the hint', max_length=400)),
                ('request_time', models.DateTimeField(help_text=b'Hint request time')),
                ('response', models.CharField(help_text=b'The text of the response to the hint request', max_length=400)),
                ('response_time', models.DateTimeField(help_text=b'Hint request time')),
                ('last_modified_time', models.DateTimeField(help_text=b'Last time of modification')),
                ('puzzle', models.ForeignKey(help_text=b'The puzzle that this hint is related to', on_delete=django.db.models.deletion.CASCADE, to='huntserver.Puzzle')),
                ('team', models.ForeignKey(help_text=b'The team that requested the hint', on_delete=django.db.models.deletion.CASCADE, to='huntserver.Team')),
            ],
        ),
    ]
