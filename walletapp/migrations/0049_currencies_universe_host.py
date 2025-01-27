# Generated by Django 4.1.4 on 2023-09-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "walletapp",
            "0048_remove_transactions_check_transaction_status_consistency_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="currencies",
            name="universe_host",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Universe host associated with the currency.",
                max_length=50000,
                null=True,
            ),
        ),
    ]
