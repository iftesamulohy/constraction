# Generated by Django 4.2.3 on 2023-09-14 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0009_alter_loaninstallment_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanlog',
            name='activity',
            field=models.TextField(blank=True, null=True),
        ),
    ]
