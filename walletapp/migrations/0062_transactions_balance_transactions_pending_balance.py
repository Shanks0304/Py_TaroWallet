# Generated by Django 4.1.4 on 2023-11-24 12:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("walletapp", "0061_alter_currencies_options_alter_currencies_supply"),
    ]

    operations = [
        migrations.AddField(
            model_name="transactions",
            name="balance",
            field=models.IntegerField(
                default=0,
                help_text="User balance",
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
        migrations.AddField(
            model_name="transactions",
            name="pending_balance",
            field=models.IntegerField(
                default=0,
                help_text="User pending balance",
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
    ]