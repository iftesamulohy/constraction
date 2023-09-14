# Generated by Django 4.2.3 on 2023-09-12 05:08

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loan', '0006_remove_loanbeneficaries_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loantransactions',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.date(2023, 9, 12), null=True),
        ),
        migrations.CreateModel(
            name='LoanInstallment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
                ('instalment', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('document', models.FileField(upload_to='documents')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateField(blank=True, default=datetime.date(2023, 9, 12), null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('giver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_installment', to='loan.loanbeneficaries')),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.loantransactions')),
                ('taker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_installment', to='loan.loanbeneficaries')),
            ],
        ),
    ]