# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('sex', models.IntegerField(default=1, null=True, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(1, '\u7537'), (2, '\u5973')])),
                ('email', models.EmailField(max_length=50, verbose_name=b'\xe7\x94\xb5\xe5\xad\x90\xe9\x82\xae\xe7\xae\xb1')),
                ('password', models.CharField(default=b'123456', max_length=64, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xaf\x86\xe7\xa0\x81')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': '\u7ba1\u7406\u5458\u4fe1\u606f',
                'verbose_name_plural': '\u7ba1\u7406\u5458\u4fe1\u606f',
            },
        ),
    ]
