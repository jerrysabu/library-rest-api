from rest_framework import serializers
from . models import Category, Library

from . import models


class CategorySerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
            model = Category
            fields = '__all__'

class LibrarySerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
            model = Library
            fields = '__all__'
