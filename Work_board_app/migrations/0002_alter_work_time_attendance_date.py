# Generated by Django 4.0.4 on 2023-03-04 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work_board_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_time',
            name='attendance_date',
            field=models.DateField(default=datetime.date(2023, 3, 4), verbose_name='出勤日'),
        ),
    ]
