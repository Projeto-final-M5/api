# Generated by Django 4.1.2 on 2022-11-09 17:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("borroweds", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FeedBack",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "stars_owner",
                    models.PositiveIntegerField(
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                (
                    "stars_renter",
                    models.PositiveIntegerField(
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                ("rating_owner", models.TextField(blank=True, null=True)),
                ("rating_renter", models.TextField(blank=True, null=True)),
                (
                    "borrowed",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feed_back",
                        to="borroweds.borrowed",
                    ),
                ),
            ],
        ),
    ]
