# Generated by Django 4.1.4 on 2023-02-07 12:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("walletapp", "0026_alter_currencies_acronym_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currencies",
            name="genesis_bootstrap_info",
            field=models.CharField(
                default="",
                help_text=(
                    "Genesis bootstrap info of the asset. Required for creating an"
                    " invoice."
                ),
                max_length=10000,
                unique=True,
            ),
        ),
    ]
