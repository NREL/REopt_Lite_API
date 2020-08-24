# Generated by Django 2.2.10 on 2020-08-20 22:02

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0070_financialmodel_irr_pct'),
    ]

    operations = [
        migrations.AddField(
            model_name='windmodel',
            name='year_one_curtailed_production_series_kw',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, null=True, size=None),
        ),
    ]
