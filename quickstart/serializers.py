from hvad.contrib.restframework.serializers import TranslatableModelSerializer
from rest_framework import serializers
from models import Fruit


class FruitSerializer(TranslatableModelSerializer):
    class Meta:
        model = Fruit
        fields = ('id', 'name', 'description', 'price', 'promoted', 'language_code')

