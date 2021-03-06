# Generated by Django 3.0.5 on 2020-05-22 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_auto_20200427_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='next',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='next_cal', to='adminapp.Calendar', verbose_name='Next Calendar'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='prev',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='prev_cal', to='adminapp.Calendar', verbose_name='Previous Calendar'),
        ),
    ]
