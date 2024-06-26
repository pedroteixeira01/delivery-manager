# Generated by Django 5.0.3 on 2024-03-21 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('origin_city', models.CharField(max_length=200)),
                ('origin_state', models.CharField(max_length=4)),
                ('origin_latitude', models.FloatField()),
                ('origin_longitude', models.FloatField()),
                ('destination_city', models.CharField(max_length=200)),
                ('destination_state', models.CharField(max_length=4)),
                ('destination_latitude', models.FloatField()),
                ('destination_longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truck', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=4)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
