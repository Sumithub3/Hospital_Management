# Generated by Django 3.2.13 on 2022-05-31 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_portal', '0004_auto_20220531_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift_in_timings',
            name='entry',
            field=models.TimeField(default=datetime.time(17, 4, 22, 209262)),
        ),
        migrations.AlterField(
            model_name='shift_out_timings',
            name='out',
            field=models.TimeField(default=datetime.time(17, 4, 22, 209262)),
        ),
    ]
