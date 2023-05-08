from rest_framework import serializers
from books.serializers import BookSerializer
from .models import Copy


class CopiesSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Copy
        fields = ["id", "is_available", "last_loan", "book"]
        extra_kwargs = {"book": {"read_only": True}}
