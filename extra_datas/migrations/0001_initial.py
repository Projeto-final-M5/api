# Generated by Django 4.1.2 on 2022-11-07 21:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Extra_Data",
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
                    "additional_data",
                    models.TextField(blank=True, default=None, null=True),
                ),
                ("translater", models.CharField(blank=True, max_length=100, null=True)),
                ("translated", models.BooleanField(default=False)),
                (
                    "book",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="extra_data",
                        to="books.book",
                    ),
                ),
            ],
        ),
    ]
