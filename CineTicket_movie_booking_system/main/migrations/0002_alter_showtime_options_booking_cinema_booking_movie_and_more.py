# Generated by Django 4.2.2 on 2023-11-04 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='showtime',
            options={'ordering': ('cinema', 'showtime')},
        ),
        migrations.AddField(
            model_name='booking',
            name='cinema',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.cinema'),
        ),
        migrations.AddField(
            model_name='booking',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.movie'),
        ),
        migrations.AddField(
            model_name='booking',
            name='seats',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(null=True, upload_to='movies/images'),
        ),
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showtime',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.CharField(default='2h 45min', max_length=100),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='showtime',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.showtime')),
            ],
        ),
    ]
