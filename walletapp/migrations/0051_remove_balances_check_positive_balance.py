# Generated by Django 4.1.4 on 2023-09-28 10:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("walletapp", "0050_alter_currencies_name_alter_currencies_status_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="balances",
            name="check_positive_balance",
        ),
    ]
