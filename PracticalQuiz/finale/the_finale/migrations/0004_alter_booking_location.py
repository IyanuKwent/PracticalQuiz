# Generated by Django 5.1.6 on 2025-02-13 00:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_finale', '0003_location_alter_booking_payment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='the_finale.location'),
        ),
    ]
