# Generated by Django 4.2.3 on 2023-09-14 05:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp2', '0021_alter_common_created_at_alter_introinfo_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='common',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 14, 11, 20, 41, 987830), null=True),
        ),
        migrations.AlterField(
            model_name='introinfo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 14, 11, 20, 41, 987830), null=True),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 14, 11, 20, 41, 987830), null=True),
        ),
    ]
