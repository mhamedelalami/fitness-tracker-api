# Generated by Django 5.2.4 on 2025-07-31 20:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Activity",
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
                    "activity_type",
                    models.CharField(
                        choices=[
                            ("running", "Running"),
                            ("cycling", "Cycling"),
                            ("walking", "Walking"),
                            ("swimming", "Swimming"),
                            ("other", "Other"),
                        ],
                        max_length=20,
                    ),
                ),
                ("duration_minutes", models.PositiveIntegerField()),
                ("distance_km", models.FloatField(blank=True, null=True)),
                ("calories_burned", models.PositiveIntegerField()),
                ("date", models.DateField()),
                ("notes", models.TextField(blank=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
