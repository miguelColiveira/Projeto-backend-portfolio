from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from books.models import Book
from books.serializer import BookSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsCollaborator


class BookView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]

    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]

    queryset = Book
    serializer_class = BookSerializer
