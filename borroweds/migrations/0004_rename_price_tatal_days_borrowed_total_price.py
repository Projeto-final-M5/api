# Generated by Django 4.1.2 on 2022-11-07 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("borroweds", "0003_borrowed_price_tatal_days"),
    ]

    operations = [
        migrations.RenameField(
            model_name="borrowed",
            old_name="price_tatal_days",
            new_name="total_price",
        ),
    ]
