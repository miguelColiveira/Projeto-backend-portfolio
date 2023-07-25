from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken
from copies.models import Copy
from copies.serializer import CopySerializer
from users.serializers import UserSerializer
from books_follow.models import BookFollow


class BookFollowSerializer(serializers.ModelSerializer):
    copy = CopySerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = BookFollow
        fields = ["id", "copy", "user"]


def create(self, validated_data: dict):
    token = self.context["request"].auth.token
    decoded_token = AccessToken(token)

    user_id = decoded_token["user_id"]
    copy_id = self.context["view"].kwargs["copy_id"]

    copy = Copy.objects.get(id=copy_id)

    return BookFollow.objects.create(
        **validated_data,
        user_id=user_id,
        copy_id=copy_id,
    )
