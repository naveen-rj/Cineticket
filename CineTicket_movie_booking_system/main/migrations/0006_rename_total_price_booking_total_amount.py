# Generated by Django 4.2.2 on 2023-11-07 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_showtime_booking_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='total_price',
            new_name='total_amount',
        ),
    ]
