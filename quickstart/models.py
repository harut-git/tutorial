from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    price = models.IntegerField()
    promoted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
