# Generated by Django 4.2.3 on 2023-08-31 03:59

import datetime
from django.db import migrations, models

def convert_active_to_boolean(apps, schema_editor):
    MyModel = apps.get_model('globalapp2', 'introinfo')
    MyModel.objects.filter(status='Active').update(status=True)
class Migration(migrations.Migration):

    dependencies = [
        ('globalapp2', '0019_alter_introinfo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introinfo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 31, 9, 59, 55, 526912), null=True),
        ),
        migrations.AlterField(
            model_name='introinfo',
            name='status',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.RunPython(convert_active_to_boolean),
    ]