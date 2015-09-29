# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminuser',
            name='nickname',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='adminuser',
            name='password',
            field=models.CharField(default=b'', max_length=64, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xaf\x86\xe7\xa0\x81'),
        ),
    ]
