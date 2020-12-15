from django.shortcuts import render
from rest_framework import generics, filters
from . models import Library
from . serializers import LibrarySerializer
# Create your views here.

class LibraryAPIView(generics.ListCreateAPIView):

    search_fields = ['name','price']
    filter_backends = (filters.SearchFilter,)
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
