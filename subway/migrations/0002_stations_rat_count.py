# Generated by Django 4.0.4 on 2022-04-27 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subway', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stations',
            name='rat_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
