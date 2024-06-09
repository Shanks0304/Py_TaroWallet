# Generated by Django 4.1.4 on 2023-02-03 12:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("walletapp", "0022_alter_transactions_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="transactions",
            name="destination_user",
            field=models.ForeignKey(
                blank=True,
                help_text="Internal user who has received the transaction",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="user2user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="user",
            field=models.ForeignKey(
                blank=True,
                help_text="User who executed the transaction",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="owner",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
