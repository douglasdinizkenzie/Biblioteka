from rest_framework import serializers
from .models import Followings
from .models import Book
from users.serializers import UserSerializer


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
        fields = ["id", "title", "sinopse", "author", "year", "copies", "followings"]
        extra_kwargs = {"copies": {"read_only": True}}
        depth = 1


class FollowingSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Followings
        fields = ["book", "users"]