# Generated by Django 4.2.3 on 2023-07-17 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_myuser_is_vendor_myuser_is_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='joined_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 17, 19, 50, 12, 733686), null=True),
        ),
    ]
