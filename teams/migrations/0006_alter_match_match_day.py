# Generated by Django 5.0.4 on 2024-04-28 00:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_alter_match_match_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_day',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 21, 3, 51, 61101), null=True),
        ),
    ]
