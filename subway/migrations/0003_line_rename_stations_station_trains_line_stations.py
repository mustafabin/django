# Generated by Django 4.0.4 on 2022-04-27 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subway', '0002_stations_rat_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1)),
                ('express', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameModel(
            old_name='Stations',
            new_name='Station',
        ),
        migrations.CreateModel(
            name='Trains',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subway.line')),
            ],
        ),
        migrations.AddField(
            model_name='line',
            name='stations',
            field=models.ManyToManyField(to='subway.station'),
        ),
    ]
