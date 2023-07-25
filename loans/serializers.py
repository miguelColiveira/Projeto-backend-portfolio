from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken
from copies.models import Copy
from loans.models import Loan
from datetime import datetime, timedelta


class LoanSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    return_date = serializers.DateTimeField(read_only=True)
    copy_id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data: dict):
        token = self.context["request"].auth.token
        decoded_token = AccessToken(token)

        return_date = datetime.now() + timedelta(days=7)
        if return_date.weekday() == 5:
            return_date = return_date + timedelta(days=2)
        if return_date.weekday() == 6:
            return_date = return_date + timedelta(days=1)

        user_id = decoded_token["user_id"]
        copy_id = self.context["view"].kwargs["copy_id"]

        copy = Copy.objects.get(id=copy_id)

        copy.active_loan = True
        copy.save()

        return Loan.objects.create(
            **validated_data,
            user_id=user_id,
            copy_id=copy_id,
            return_date=return_date
        )
