from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination


# Create your views here.

class categoryViewset(viewsets.ModelViewSet):
    queryset = models.category.objects.all()
    serializer_class = serializers.CategorySerializer

# class flowerPagination(pagination.PageNumberPagination):
#     page_size = 2 # items per page
#     page_size_query_param = page_size
#     max_page_size = 100

class flowerViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
 
    queryset = models.flower.objects.all()
    serializer_class = serializers.flowerSerializer
    filter_backends = [filters.SearchFilter]
    # pagination_class = flowerPagination
    search_fields = ['title','categories__name']