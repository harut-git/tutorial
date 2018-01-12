from hvad.contrib.restframework.serializers import TranslatableModelSerializer
from rest_framework import serializers
from models import Product, Fruit


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')


class FruitSerializer(TranslatableModelSerializer):
    class Meta:
        model = Fruit
        fields = ('name', 'description', 'price', 'promoted')
