# Generated by Django 5.0.2 on 2024-02-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=120)),
                ("author", models.CharField(max_length=60)),
                (
                    "cover",
                    models.CharField(
                        choices=[("HARD", "Hard"), ("SOFT", "Soft")], max_length=4
                    ),
                ),
                ("inventory", models.PositiveIntegerField(default=0)),
                ("daily_free", models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
