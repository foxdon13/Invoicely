# Generated by Django 3.2.6 on 2021-09-01 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_invoice_is_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='vet_amount',
            new_name='vat_amount',
        ),
    ]
