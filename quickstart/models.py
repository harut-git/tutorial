from __future__ import unicode_literals

import uuid

from django.db import models
from hvad.models import TranslatableModel, TranslatedFields


# Create your models here.


class Fruit(TranslatableModel):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    promoted = models.BooleanField(default=False)

    translations = TranslatedFields(
        name=models.TextField(),
        description=models.CharField(max_length=255)
    )

    def __str__(self):
        # return "name" from translation
        return self.safe_translation_getter('name', str(self.pk))
