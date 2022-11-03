# Generated by Django 4.1.2 on 2022-11-03 16:25

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
            name="Picture",
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
                ("picture", models.TextField(blank=True, null=True)),
                (
                    "book",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="picture",
                        to="books.book",
                    ),
                ),
            ],
        ),
    ]
