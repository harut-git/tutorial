from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin

from models import Product, Fruit
from django_filters.rest_framework import DjangoFilterBackend

from serializers import ProductSerializer, FruitSerializer


# Create your views here.

class Products(generics.CreateAPIView):
    serializer_class = ProductSerializer


class ProductViewSet(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        queryset = Product.objects.all()
        queryset.filter()
        return Product.objects.filter(name=name)


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'price')


class FruitList(generics.ListAPIView):
    serializer_class = FruitSerializer

    def get_queryset(self):
        queryset = Fruit.objects.language(self.request.query_params.get('lang', None)).all()
        return queryset


class Fruits(generics.CreateAPIView):
    serializer_class = FruitSerializer


class FruitsUpdate(generics.UpdateAPIView):
    serializer_class = FruitSerializer

    def get_queryset(self):
        fruit_id = self.kwargs['pk']
        return Fruit.objects.filter(id=fruit_id)


class FruitPartialUpdateView(GenericAPIView, UpdateModelMixin):
    '''
    You just need to provide the field which is to be modified.
    '''
    serializer_class = FruitSerializer

    def get_queryset(self):
        fruit_id = self.kwargs['pk']
        return Fruit.objects.filter(id=fruit_id)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)