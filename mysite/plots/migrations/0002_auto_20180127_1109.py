# Generated by Django 2.0.1 on 2018-01-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plot',
            name='acreage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='plot',
            name='bed_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='plot',
            name='lines_per_bed',
            field=models.IntegerField(),
        ),
    ]
