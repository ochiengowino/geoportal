# Generated by Django 5.0.2 on 2024-03-15 11:06

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo_app', '0003_counties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counties',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=-1),
        ),
    ]
