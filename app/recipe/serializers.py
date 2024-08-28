"""
Serializers for recipe APIs.
"""
from rest_framework import serializers  # type: ignore

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializers):
    """Serializer for recipes."""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minuets', 'price', 'link']
        read_only = ['id']
