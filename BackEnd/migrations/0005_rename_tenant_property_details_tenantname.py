# Generated by Django 4.2.5 on 2024-01-07 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0004_property_details_propertytype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property_details',
            old_name='Tenant',
            new_name='TenantName',
        ),
    ]
