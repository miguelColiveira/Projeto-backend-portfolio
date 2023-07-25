from rest_framework import serializers
from books.models import Book

from copies.models import Copy


class CopySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    book_title = serializers.ReadOnlyField(source="book.title")
    active_loan = serializers.BooleanField(read_only=True)
    book_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        book_id = self.context["view"].kwargs["pk"]

        book = Book.objects.get(id=book_id)

        book.copies = book.copies + 1
        book.save()

        return Copy.objects.create(**validated_data, book_id=book_id)
