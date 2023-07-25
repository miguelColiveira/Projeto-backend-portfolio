from rest_framework import serializers

from books.models import Book

from rest_framework_simplejwt.tokens import AccessToken

from users.models import User

from datetime import datetime


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=255, default=None)
    publisher = serializers.CharField(max_length=50)
    published_at = serializers.DateTimeField(read_only=True)
    copies = serializers.IntegerField(allow_null=False, default=0)
    user_id = serializers.ReadOnlyField()

    def update(self, instance: Book, validated_data: dict) -> Book:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    def create(self, validated_data: dict):
        token = self.context["request"].auth.token
        decoded_token = AccessToken(token)
        user_id = decoded_token["user_id"]

        return Book.objects.create(**validated_data, user_id=user_id)
