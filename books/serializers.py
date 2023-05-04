from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "sinopse", "author", "year", "copies"]
        read_only_fiels = ["copies"]
    
    def create(self, validated_data):
        return Book.objects.create(**validated_data)