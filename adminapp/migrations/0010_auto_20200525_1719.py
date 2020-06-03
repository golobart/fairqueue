# Generated by Django 3.0.5 on 2020-05-25 15:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_auto_20200525_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daysoff',
            name='week_day',
            field=models.CharField(max_length=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)]),
        ),
    ]