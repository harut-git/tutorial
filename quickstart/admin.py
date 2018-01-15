import hvad
from django.contrib import admin

# Register your models here.
from hvad.admin import TranslatableAdmin

from quickstart.models import Fruit


class FruitAdmin(TranslatableAdmin):
    def get_available_languages(self, obj):
        pass


admin.site.register(Fruit, FruitAdmin)