from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Book
from .serializers import BookSerializer
from .permissions import CollaboratorCreateBook

# Create your views here.

class BookView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CollaboratorCreateBook]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        return serializer.save()
