# Generated by Django 5.0.2 on 2024-03-15 10:33

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_app', '0002_rename_email_id_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=20, null=True)),
                ('total_pop', models.BigIntegerField(null=True)),
                ('covidcases', models.IntegerField(null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=-1)),
            ],
        ),
    ]
