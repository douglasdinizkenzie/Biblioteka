from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from books.models import Book
from .serializers import CopiesSerializer
from .models import Copy, Book_loans
from .permissions import IsAdm
from users.serializers import BookLoanSerializer
from .models import Book_loans
from users.models import User
from datetime import datetime


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
    queryset = Copy.objects.all()

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdm]

    def perform_create(self, serializer):
        book_id = get_object_or_404(Book, pk=self.kwargs["pk"])
        serializer.save(book=book_id)


class BookLoanView(RetrieveUpdateDestroyCreateAPIView):
    serializer_class = BookLoanSerializer
    queryset = Book_loans

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdm]

    def perform_create(self, serializer):
        user_id = get_object_or_404(User, pk=self.kwargs["pk"])
        copy = get_object_or_404(Copy, pk=self.request.data["copy"])
        if copy.is_available == False:
            data = {"message": "Copy already borrowed!"}
            raise ValidationError(data, code=409)
        copy.is_available = False
        copy.last_loan = datetime.now()
        copy.save()

        return serializer.save(user=user_id)

    def perform_update(self, serializer):
        loan = get_object_or_404(Book_loans, pk=self.kwargs["pk"])
        user = User.objects.get(pk=loan.user.id)

        day_time = datetime.now().timestamp()
        finish_date = loan.finished_at.timestamp()
        result = day_time - finish_date
        if result > 0:
            user.is_blocked = True
            user.save()
        