# Generated by Django 4.1.2 on 2022-11-02 13:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Borrowed",
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
                ("initial_date", models.DateField(auto_now_add=True)),
                ("finish_date", models.DateField(null=True)),
                (
                    "shipping_method",
                    models.CharField(
                        choices=[("Correio", "Correio"), ("Retirada", "Retirada")],
                        max_length=100,
                    ),
                ),
            ],
        ),
    ]
