# Generated by Django 4.1.5 on 2023-01-25 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Donators",
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
                ("food_listing", models.CharField(max_length=200)),
                ("food_quantity", models.IntegerField(default=1)),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
            ],
        ),
    ]
