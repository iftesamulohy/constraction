# Generated by Django 4.2.3 on 2023-07-17 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_myuser_first_name_myuser_joined_at_myuser_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='joined_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 17, 19, 6, 3, 853180), null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Banned', 'Banned')], max_length=50, null=True),
        ),
    ]
