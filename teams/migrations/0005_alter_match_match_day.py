# Generated by Django 5.0.4 on 2024-04-27 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_alter_match_match_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_day',
            field=models.DateTimeField(),
        ),
    ]
