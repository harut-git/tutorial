from rest_framework import viewsets, generics
from models import Product

from serializers import ProductSerializer


# Create your views here.

class Products(generics.CreateAPIView):
    serializer_class = ProductSerializer


class ProductViewSet(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        name = self.kwargs['name']
        return Product.objects.filter(name=name)
