# Generated by Django 4.1.4 on 2023-01-31 14:30

import django_s3_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("walletapp", "0009_alter_currencies_picture_large_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currencies",
            name="picture_large",
            field=models.ImageField(
                blank=True,
                default="uploads/currencies_large/default.png",
                help_text="Small icon representing the asset",
                null=True,
                storage=django_s3_storage.storage.S3Storage(
                    aws_s3_bucket_name="django-images-testnet"
                ),
                upload_to="uploads/currencies_small",
            ),
        ),
        migrations.AlterField(
            model_name="currencies",
            name="picture_small",
            field=models.ImageField(
                blank=True,
                default="uploads/currencies_large/default.png",
                help_text="Image representing the asset",
                null=True,
                storage=django_s3_storage.storage.S3Storage(
                    aws_s3_bucket_name="django-images-testnet"
                ),
                upload_to="uploads/currencies_large",
            ),
        ),
    ]
