# Generated by Django 4.0.4 on 2023-03-04 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work_board_app', '0002_alter_work_time_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_time',
            name='attendance_date',
            field=models.DateField(verbose_name='出勤日'),
        ),
    ]
