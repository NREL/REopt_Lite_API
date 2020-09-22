# Generated by Django 2.2.10 on 2020-09-22 16:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0072_auto_20200902_2126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generatormodel',
            old_name='year_one_emissions_bau_lb_C02',
            new_name='year_one_nonscope_emissions_bau_lb_C02',
        ),
        migrations.RenameField(
            model_name='generatormodel',
            old_name='year_one_emissions_lb_C02',
            new_name='year_one_nonscope_emissions_lb_C02',
        ),
        migrations.AddField(
            model_name='electrictariffmodel',
            name='year_one_emissions_series_bau_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='electrictariffmodel',
            name='year_one_emissions_series_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='generatormodel',
            name='year_one_nonscope_emissions_series_bau_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='generatormodel',
            name='year_one_nonscope_emissions_series_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='generatormodel',
            name='year_one_scope1_emissions_bau_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generatormodel',
            name='year_one_scope1_emissions_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generatormodel',
            name='year_one_scope1_emissions_series_bau_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='generatormodel',
            name='year_one_scope1_emissions_series_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='pvmodel',
            name='year_one_nonscope_emissions_bau_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvmodel',
            name='year_one_nonscope_emissions_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvmodel',
            name='year_one_nonscope_emissions_series_bau_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='pvmodel',
            name='year_one_nonscope_emissions_series_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='pvmodel',
            name='year_one_scope1_emissions_bau_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvmodel',
            name='year_one_scope1_emissions_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvmodel',
            name='year_one_scope1_emissions_series_bau_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='pvmodel',
            name='year_one_scope1_emissions_series_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_emissions_bau_input_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_emissions_reduction_bau_pct',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_nonscope_emissions_bau_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_nonscope_emissions_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_nonscope_emissions_series_bau_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_renewable_generation_bau_kwh',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_renewable_generation_bau_pct',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_scope1_emissions_bau_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_scope1_emissions_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_scope1_emissions_series_bau_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_scope2_emissions_bau_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_scope2_emissions_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_scope2_emissions_series_bau_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='windmodel',
            name='year_one_nonscope_emissions_bau_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='windmodel',
            name='year_one_nonscope_emissions_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='windmodel',
            name='year_one_nonscope_emissions_series_bau_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='windmodel',
            name='year_one_nonscope_emissions_series_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='windmodel',
            name='year_one_scope1_emissions_bau_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='windmodel',
            name='year_one_scope1_emissions_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='windmodel',
            name='year_one_scope1_emissions_series_bau_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='windmodel',
            name='year_one_scope1_emissions_series_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
    ]
