# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminuser', '0002_auto_20150929_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='TControllerlog',
            fields=[
                ('loginname', models.CharField(max_length=16, serialize=False, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9clog', primary_key=True, db_column=b'Loginname')),
                ('action', models.CharField(max_length=64, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c', db_column=b'Action')),
                ('action_time', models.DateField(verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4', db_column=b'Action_time')),
                ('remark', models.CharField(max_length=100, verbose_name=b'\xe8\xae\xb0\xe5\xbd\x95')),
            ],
            options={
                'db_table': 't_controllerlog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TControllers',
            fields=[
                ('loginname', models.CharField(primary_key=True, db_column=b'Loginname', serialize=False, max_length=16, unique=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=32, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('permit', models.IntegerField(default=1, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe6\x9d\x83\xe9\x99\x90', choices=[(1, '\u540e\u53f0\u7ba1\u7406\u5458'), (2, '\u73b0\u573a\u7ba1\u7406\u5458')])),
                ('flag', models.IntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\xa6\x81\xe7\x94\xa8', choices=[(0, '\u542f\u7528'), (1, '\u7981\u7528')])),
            ],
            options={
                'verbose_name': 'Controller',
                'db_table': 't_controllers',
                'managed': False,
                'verbose_name_plural': 'Controllers',
            },
        ),
        migrations.DeleteModel(
            name='AdminUser',
        ),
    ]
