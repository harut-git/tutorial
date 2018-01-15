from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin

from models import Fruit
from serializers import FruitSerializer


# Create your views here.

class Fruits(generics.ListCreateAPIView):
    serializer_class = FruitSerializer

    def get_queryset(self):
        fruit_id = self.kwargs.get('pk', None)
        if fruit_id is not None:
            queryset = Fruit.objects.language(self.request.query_params.get('lang', None)).filter(id=fruit_id)
        else:
            queryset = Fruit.objects.language(self.request.query_params.get('lang', None)).all()
        return queryset


class FruitPartialUpdateView(GenericAPIView, UpdateModelMixin):
    '''
    You just need to provide the field which is to be modified.
    '''
    queryset = Fruit.objects.language('en').all()
    serializer_class = FruitSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)