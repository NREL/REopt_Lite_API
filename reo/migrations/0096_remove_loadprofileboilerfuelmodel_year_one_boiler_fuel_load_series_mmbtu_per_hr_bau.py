# Generated by Django 2.2.13 on 2021-01-14 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0095_chpmodel_cooling_thermal_factor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loadprofileboilerfuelmodel',
            name='year_one_boiler_fuel_load_series_mmbtu_per_hr_bau',
        ),
    ]
