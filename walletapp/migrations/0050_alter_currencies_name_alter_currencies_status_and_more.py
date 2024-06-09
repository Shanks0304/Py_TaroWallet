# Generated by Django 4.1.4 on 2023-09-26 01:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("walletapp", "0049_currencies_universe_host"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currencies",
            name="name",
            field=models.CharField(
                help_text=(
                    "Cryptocurrency name represented as word. e.g. Bitcoin, Ethereum"
                ),
                max_length=30,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9a-zA-Z]*$", "Only alphanumeric characters are allowed."
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="currencies",
            name="status",
            field=models.CharField(
                choices=[
                    (
                        "waiting_for_miting_transaction",
                        "Waiting for minting transaction",
                    ),
                    ("submitted_for_minting", "Submitted for minting"),
                    ("minting", "Minting"),
                    ("minted", "Minted"),
                    ("error", "Error"),
                    ("waiting_for_meta_data", "Waiting for metadata"),
                    (
                        "waiting_for_create_transaction",
                        "Waiting for create transaction",
                    ),
                    ("minted", "Minted"),
                ],
                default="",
                help_text="Status of the minting transaction",
                max_length=50,
            ),
        ),
        migrations.AddConstraint(
            model_name="balances",
            constraint=models.CheckConstraint(
                check=models.Q(("balance__gte", 0), ("pending_balance__gte", 0)),
                name="check_positive_balance",
            ),
        ),
    ]
