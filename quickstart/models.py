from __future__ import unicode_literals

import uuid

from django.db import models
from hvad.models import TranslatableModel, TranslatedFields


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    price = models.IntegerField()
    promoted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Fruit(TranslatableModel):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    promoted = models.BooleanField(default=False)

    translations = TranslatedFields(
        name=models.TextField(),
        description=models.CharField(max_length=255)
    )
