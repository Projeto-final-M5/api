from django.db import models
import uuid
# Create your models here.

class Options(models.TextChoices):
    CORREIO   = "Correio"
    RETIRADA  = "Retirada"


class Borrowed(models.Model):
    id                 = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    initial_date       = models.DateField(auto_now_add=True)
    finish_date        = models.DateField(null = True)
    shipping_method    = models.CharField(max_length=100, choices=Options.choices)
    
    #book_borrowed = models.ForeignKey("", on_delete=models.CASCADE, related_name="borroweds")