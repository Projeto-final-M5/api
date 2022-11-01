from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

import uuid

from borroweds.models import Borrowed


class User(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    avatar = models.TextField(
        null=True,
        blank=True,
        default=None,
    )
    email = models.EmailField()
    birth = models.DateField()
    stars = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=5,
        editable=False,
    )

    # borrowed = models.ManyToManyField(Borrowed, on_delete=models.CASCADE)

    REQUIRED_FIELDS = [
        "email",
        "birth",
    ]
