# Generated by Django 4.2.6 on 2023-11-01 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crms', '0022_rename_registereddate_customer_registered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
