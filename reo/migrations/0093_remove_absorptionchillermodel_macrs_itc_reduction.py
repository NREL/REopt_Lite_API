# Generated by Django 2.2.10 on 2021-01-04 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0092_auto_20201230_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='absorptionchillermodel',
            name='macrs_itc_reduction',
        ),
    ]
