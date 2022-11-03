from django.db import models

import uuid

from users.models import User


class AddressState(models.TextChoices):
    UNDEFINED = None


class AddressCity(models.TextChoices):
    UNDEFINED = None


class AddressPlace(models.TextChoices):
    UNDEFINED = None


class Address(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    state = models.CharField(
        max_length=100,
        choices=AddressState.choices,
        default=AddressState.UNDEFINED,
    )
    city = models.CharField(
        max_length=100,
        choices=AddressCity.choices,
        default=AddressCity.UNDEFINED,
    )
    district = models.CharField(
        max_length=100,
    )
    place = models.CharField(
        max_length=100,
        choices=AddressPlace.choices,
        default=AddressPlace.UNDEFINED,
    )
    number = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    zip_code = models.CharField(
        max_length=8,
        null=False,
        blank=False,
    )
    additional_data = models.TextField(null=True, blank=True,)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="address")
