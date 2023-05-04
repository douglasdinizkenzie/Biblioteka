from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404
from books.models import Book
from .serializers import CopiesSerializer
from .models import Copies
from .permissions import IsAdm

# Create your views here.


class RetrieveUpdateDestroyCreateAPIView(
    generics.CreateAPIView,
    generics.RetrieveAPIView,
    generics.DestroyAPIView,
    generics.UpdateAPIView,
):
    pass


class CopiesView(RetrieveUpdateDestroyCreateAPIView):
    serializer_class = CopiesSerializer
    queryset = Copies.objects.all()

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdm]

    def perform_create(self, serializer):
        book_id = get_object_or_404(Book, pk=self.kwargs["pk"])
        serializer.save(book=book_id)
