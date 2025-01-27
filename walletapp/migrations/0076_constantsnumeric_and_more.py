# Generated by Django 4.1.4 on 2024-04-21 18:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("walletapp", "0075_alter_collections_images_zip_file_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConstantsNumeric",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        default="", help_text="Constant name", max_length=200
                    ),
                ),
                ("value", models.IntegerField(default=0, help_text="Constant value")),
            ],
        ),
        migrations.AddIndex(
            model_name="constantsnumeric",
            index=models.Index(fields=["name"], name="walletapp_c_name_c2c972_idx"),
        ),
    ]
