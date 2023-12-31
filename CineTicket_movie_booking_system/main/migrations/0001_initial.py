# Generated by Django 4.2.2 on 2023-10-20 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('runtime', models.IntegerField()),
                ('description', models.TextField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showtime', models.DateTimeField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_tickets', models.IntegerField()),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.showtime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
