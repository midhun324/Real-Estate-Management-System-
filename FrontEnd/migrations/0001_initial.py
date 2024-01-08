# Generated by Django 4.2.5 on 2024-01-07 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PropertyName', models.CharField(blank=True, max_length=50, null=True)),
                ('Description', models.CharField(blank=True, max_length=50, null=True)),
                ('Type', models.CharField(blank=True, max_length=50, null=True)),
                ('Address', models.CharField(blank=True, max_length=50, null=True)),
                ('Price', models.CharField(blank=True, max_length=50, null=True)),
                ('Size', models.CharField(blank=True, max_length=50, null=True)),
                ('Parking', models.CharField(blank=True, max_length=50, null=True)),
                ('Garage', models.CharField(blank=True, max_length=50, null=True)),
                ('PropertyStatus', models.CharField(blank=True, max_length=50, null=True)),
                ('BedRooms', models.CharField(blank=True, max_length=50, null=True)),
                ('Status', models.CharField(blank=True, max_length=50, null=True)),
                ('Bathrooms', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
