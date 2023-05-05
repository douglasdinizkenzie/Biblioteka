from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from copies.models import Book_loans
from datetime import datetime, timedelta


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(write_only=True)

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        ]

class BookLoanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Book_loans
        fields = ["id", "started_at", "finished_at", "status", "user", "copy"]
        read_only_fields = ["started_at", "finished_at", "status"]
    
    def create(self, validated_data):
        returned_date = datetime.now() + timedelta(days=7)
        check_weekend = returned_date.date().weekday()

        if check_weekend == 5:
            returned_date += timedelta(days=2)

        if check_weekend == 6:
            returned_date += timedelta(days=1)
        
        validated_data["finished_at"] = returned_date

        return Book_loans.objects.create(**validated_data)


class UserDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(write_only=True)

    is_superuser = serializers.BooleanField(read_only=True)

    #loans = BookLoanSerializer(many=True, read_only=True)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(instance.password)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "is_superuser",
            "is_blocked",
            "is_student",
            "email",
            "password",
            "loans",
        ]
        depth = 2
