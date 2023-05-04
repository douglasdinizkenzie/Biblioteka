from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance: Book, validated_data: dict) -> Book:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Book
        fields = ["id", "title", "sinopse", "author", "year", "copies"]
        extra_kwargs = {"copies": {"read_only": True}}
