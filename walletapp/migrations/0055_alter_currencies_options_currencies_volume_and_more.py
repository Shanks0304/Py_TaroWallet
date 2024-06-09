# Generated by Django 4.1.4 on 2023-11-08 10:03

import django.core.validators
import django.db.models.deletion
import django_s3_storage.storage
import walletapp.utils
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "walletapp",
            "0054_remove_transactions_check_transaction_status_consistency_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="currencies",
            options={"ordering": ["-volume"]},
        ),
        migrations.AddField(
            model_name="currencies",
            name="volume",
            field=models.IntegerField(
                blank=True,
                default=0,
                help_text="Volume of the asset traded in last 1 hour",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="listings",
            name="amount",
            field=models.IntegerField(
                blank=True,
                default=0,
                help_text="Amount of currency to be exchanged",
                null=True,
                validators=[django.core.validators.MinValueValidator(1)],
            ),
        ),
        migrations.AddField(
            model_name="listings",
            name="type",
            field=models.CharField(
                choices=[
                    ("order_bid", "Bid - Offering SATs in exchange for Taproot Assets"),
                    (
                        "order_ask",
                        "Ask - Asking for SATs in exchange for Taproot Assets",
                    ),
                    ("lp", "Listing of currency with liquidity pool"),
                ],
                default="lp",
                help_text="Type of listing - Bid or Ask",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="pricehistory",
            name="orders",
            field=models.CharField(
                default="",
                help_text="JSON list of all orders closed in this time period",
                max_length=5000,
            ),
        ),
        migrations.AddField(
            model_name="transactions",
            name="listing",
            field=models.ForeignKey(
                blank=True,
                help_text="Listing the transaction is executed from.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="walletapp.listings",
            ),
        ),
        migrations.AlterField(
            model_name="currencies",
            name="picture_large",
            field=models.ImageField(
                blank=True,
                help_text="Small icon representing the asset",
                null=True,
                storage=django_s3_storage.storage.S3Storage(
                    aws_s3_bucket_name="django-images-prod"
                ),
                upload_to=walletapp.utils.get_media_path_large,
            ),
        ),
        migrations.AlterField(
            model_name="currencies",
            name="picture_orig",
            field=models.ImageField(
                blank=True,
                help_text=(
                    "Image representing the asset. Please upload a square image about"
                    " 800x800 in size. Images will be rescaled."
                ),
                null=True,
                storage=django_s3_storage.storage.S3Storage(
                    aws_s3_bucket_name="django-images-prod"
                ),
                upload_to=walletapp.utils.get_media_path_orig,
            ),
        ),
        migrations.AlterField(
            model_name="currencies",
            name="picture_small",
            field=models.ImageField(
                blank=True,
                help_text="Large icon representing the asset",
                null=True,
                storage=django_s3_storage.storage.S3Storage(
                    aws_s3_bucket_name="django-images-prod"
                ),
                upload_to=walletapp.utils.get_media_path_small,
            ),
        ),
        migrations.AlterField(
            model_name="listings",
            name="currency",
            field=models.ForeignKey(
                blank=True,
                help_text="Taproot Asset to be exchanged",
                on_delete=django.db.models.deletion.CASCADE,
                to="walletapp.currencies",
            ),
        ),
        migrations.AlterField(
            model_name="listings",
            name="price_sat",
            field=models.DecimalField(
                blank=True,
                decimal_places=5,
                default=0,
                help_text="Price in SATs that the asset should be exchanged for.",
                max_digits=15,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="status",
            field=models.CharField(
                choices=[
                    (
                        "inbound_invoice_waiting_for",
                        "Waiting for inbound invoice to be generated",
                    ),
                    (
                        "inbound_invoice_generated",
                        "Inbound invoice was generated, waiting for it to be paid",
                    ),
                    ("inbound_invoice_paid", "Inbound invoice was successfully paid"),
                    (
                        "outbound_invoice_received",
                        "Outbound invoice is waiting to be paid",
                    ),
                    ("outbound_invoice_paid", "Outbound invoice paid"),
                    ("placeholder_fee", "Placeholder fee, real amount will be added"),
                    ("fee_paid", "Fee paid"),
                    ("minting_submitted", "Currency submitted for minting"),
                    ("minting", "Currency is minting"),
                    ("tx_created", "Minting transaction created"),
                    ("minted", "Minting transaction was completed"),
                    ("internal_stated", "Internal transaction submitted"),
                    ("internal_finished", "Internal transaction finished"),
                    ("exchange_started", "Exchange transaction submitted"),
                    ("exchange_finished", "Exchange transaction finished"),
                    (
                        "replaced_with_internal_transaction",
                        "This transaction was replaced with internal transaction to"
                        " save fees",
                    ),
                    ("waiting_for_meta_data", "Waiting for currency metadata"),
                    (
                        "currency_registration_finished",
                        "Registration of a new currency is finished.",
                    ),
                    ("error", "Error"),
                ],
                default="",
                help_text="Transaction status",
                max_length=50,
            ),
        ),
        migrations.AddConstraint(
            model_name="currencies",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(("is_nft", True), ("supply", 1)),
                    models.Q(("is_nft", False), ("supply__gt", 0)),
                    _connector="OR",
                ),
                name="suppy_for_nft_assets_has_to_be_one",
            ),
        ),
        migrations.AddConstraint(
            model_name="currencies",
            constraint=models.UniqueConstraint(
                fields=("is_nft", "name"), name="name_unique"
            ),
        ),
        migrations.AddConstraint(
            model_name="listings",
            constraint=models.UniqueConstraint(
                condition=models.Q(("type", "lp")),
                fields=("currency",),
                name="one_lp_per_currency",
            ),
        ),
        migrations.AddConstraint(
            model_name="listings",
            constraint=models.UniqueConstraint(
                condition=models.Q(("type", "order_ask")),
                fields=("user", "currency"),
                name="one_order_ask_per_user_currency",
            ),
        ),
        migrations.AddConstraint(
            model_name="listings",
            constraint=models.UniqueConstraint(
                condition=models.Q(("type", "order_bid")),
                fields=("user", "currency"),
                name="one_order_bid_per_user_currency",
            ),
        ),
    ]