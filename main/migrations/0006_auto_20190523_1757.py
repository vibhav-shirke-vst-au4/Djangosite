# Generated by Django 2.2.1 on 2019-05-23 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190523_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 23, 17, 57, 5, 227498), verbose_name='date published'),
        ),
    ]
