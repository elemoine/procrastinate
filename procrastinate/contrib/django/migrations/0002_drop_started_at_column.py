# Generated by Django 3.1 on 2020-08-22 16:57

from django.db import migrations

import procrastinate.contrib.django.utils


class Migration(migrations.Migration):

    dependencies = [
        ("procrastinate", "0001_baseline"),
    ]

    operations = [
        procrastinate.contrib.django.utils.RunProcrastinateFile(
            filename="delta_0.5.0_002_drop_started_at_column.sql",
        ),
    ]
