# Generated by Django 3.2.6 on 2021-09-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_rename_vet_amount_invoice_vat_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='bankaccount',
            field=models.CharField(blank=True, max_length=266, null=True),
        ),
    ]
