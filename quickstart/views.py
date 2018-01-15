from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin

from models import Fruit
from serializers import FruitSerializer


# Create your views here.

class Fruits(generics.ListCreateAPIView):
    serializer_class = FruitSerializer

    def get_queryset(self):
        queryset = Fruit.objects.language(self.request.query_params.get('lang', None))
        fruit_id = self.request.query_params.get('id', None)
        promoted = self.request.query_params.get('promoted', None)
        if fruit_id is not None:
            queryset = queryset.filter(id=fruit_id)
        elif promoted is not None:
            queryset = queryset.filter(promoted=promoted)
        else:
            queryset.language(self.request.query_params.get('lang', None)).all()

        return queryset


class FruitPartialUpdateView(GenericAPIView, UpdateModelMixin):
    '''
    You just need to provide the field which is to be modified.
    '''
    queryset = Fruit.objects.language('en').all()
    serializer_class = FruitSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)