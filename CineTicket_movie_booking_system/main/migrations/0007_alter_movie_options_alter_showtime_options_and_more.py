# Generated by Django 4.2.2 on 2023-11-20 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_total_price_booking_total_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('-release_date',)},
        ),
        migrations.AlterModelOptions(
            name='showtime',
            options={'ordering': ('cinema', '-date')},
        ),
        migrations.RemoveField(
            model_name='movie',
            name='cinema',
        ),
        migrations.AddField(
            model_name='movie',
            name='cinemas',
            field=models.ManyToManyField(to='main.cinema'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(default='Action | Thriller', max_length=255),
        ),
    ]