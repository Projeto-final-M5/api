from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from feed_back.models import  FeedBack
from borroweds.models import Borrowed
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

    REQUIRED_FIELDS = [
        "email",
        "birth",
    ]

    def get_nota(self, obj)-> str:
        feed_user = FeedBack.objects.filter(borrowed__user=obj)
        
        total = []
        for feed in feed_user:
            if(feed.stars_owner):
                total.append(feed.stars_owner)
                
        saida = 0
        if sum(total) != 0:
            saida = sum(total) / len(total)
        return saida