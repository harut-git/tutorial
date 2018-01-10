from rest_framework import generics
from models import Product
from django_filters.rest_framework import DjangoFilterBackend
from serializers import ProductSerializer


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
