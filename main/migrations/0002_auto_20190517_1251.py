# Generated by Django 2.2.1 on 2019-05-17 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 17, 12, 51, 29, 134646), verbose_name='date published'),
        ),
    ]
