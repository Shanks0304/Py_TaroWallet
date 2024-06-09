# Generated by Django 4.1.4 on 2024-01-12 09:22

import django_s3_storage.storage
import walletapp.utils
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("walletapp", "0064_alter_collections_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currencies",
            name="picture_large",
            field=models.ImageField(
                blank=True,
                help_text="Small icon representing the asset",
                null=True,
                storage=django_s3_storage.storage.S3Storage(
                    aws_s3_bucket_name="django-images-testnet"
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
                    aws_s3_bucket_name="django-images-testnet"
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
                    aws_s3_bucket_name="django-images-testnet"
                ),
                upload_to=walletapp.utils.get_media_path_small,
            ),
        ),
    ]
