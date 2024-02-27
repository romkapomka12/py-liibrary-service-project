# Generated by Django 5.0.2 on 2024-02-21 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("borrowing", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                    "status",
                    models.CharField(
                        choices=[("PENDING", "Pending"), ("PAID", "Paid")],
                        max_length=10,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("PAYMENT", "Payment"), ("FINE", "Fine")],
                        max_length=10,
                    ),
                ),
                ("session_url", models.URLField()),
                ("session_id", models.CharField(max_length=50)),
                ("money_to_pay", models.DecimalField(decimal_places=2, max_digits=7)),
                (
                    "borrowing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="borrowing.borrowing",
                    ),
                ),
            ],
        ),
    ]