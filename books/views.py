from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Book, Followings
from .serializers import BookSerializer, FollowingSerializer
from .permissions import CollaboratorCreateBook
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import generics
from users.permissions import IsAccountOwner
from rest_framework.response import Response


class RetrieveDestroyCreateAPIView(
    generics.CreateAPIView, generics.RetrieveAPIView, generics.DestroyAPIView
):
    pass


class BookView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CollaboratorCreateBook]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        return serializer.save()


class BookDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CollaboratorCreateBook]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = "pk"


class FollowingView(RetrieveDestroyCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Followings.objects.all()
    serializer_class = FollowingSerializer
    lookup_url_kwarg = "pk"

    def perform_create(self, serializer):
        book_id = get_object_or_404(Book, pk=self.kwargs["pk"])
        user_id = self.request.user

        follow = self.queryset.filter(book=book_id.id, user=user_id.id)

        if follow:
            raise ValidationError("You already follow this book!")

        return serializer.save(book=book_id, user=user_id)

    def destroy(self, request, *args, **kwargs):
        book_id = get_object_or_404(Book, pk=self.kwargs["pk"])
        user_id = self.request.user

        follow = self.queryset.filter(book=book_id.id, user=user_id.id)
        follow.delete()

        return Response({"message": "Book has been unfollow"})
