# Generated by Django 4.2.3 on 2023-08-11 10:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficaries',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='beneficaries',
            name='introinfo_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.introinfo'),
        ),
        migrations.AlterField(
            model_name='introinfo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 11, 16, 59, 50, 623404), null=True),
        ),
        migrations.AlterField(
            model_name='introinfo',
            name='phone_number',
            field=models.ManyToManyField(to='globalapp.phonenumber'),
        ),
    ]