from xml.parsers.expat import model
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from items.models import Item
from .serializers import ItemListSerializer, ItemDetailSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import UserCanOnlyRead, VipCanOnlyView
# from rest_framework.permissions import ba
# Create your views here.

class ItemListView(ListCreateAPIView):
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name','description']
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    permission_classes = [UserCanOnlyRead]
    
    
class ItemDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    permission_classes=[VipCanOnlyView]