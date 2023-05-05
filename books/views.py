from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Book
from .serializers import BookSerializer
from .permissions import CollaboratorCreateBook


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
