from django.shortcuts import render

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
)

from loans.models import Loan
from loans.serializers import LoanSerializer
from rest_framework.views import status, Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from copies.models import Copy
from datetime import datetime
import pytz
from django.forms.models import model_to_dict
from users.models import User
from django.shortcuts import get_object_or_404


class LoanView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Loan
    serializer_class = LoanSerializer

    def create(self, request, *args, **kwargs):
        copy_id = kwargs["copy_id"]

        copy = Copy.objects.get(id=copy_id)

        if copy.active_loan:
            return Response(
                {"message": "Livro já alugado."},
                status=status.HTTP_201_CREATED,
            )

        user_id = request.user.id
        user_loans = Loan.objects.filter(user_id=user_id)
        today = datetime.now()

        loans_list = []
        for loan in user_loans:
            loan_dict = model_to_dict(loan)
            loans_list.append(loan_dict)

        for loan in loans_list:
            if loan["return_date"].replace(tzinfo=pytz.utc) > today.replace(
                tzinfo=pytz.utc
            ):
                return Response(
                    {
                        "message": "Usuário com empréstimo vencido, realize a devolução antes de alugar outro livro"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return_data = serializer.data
        return_data["return_date"] = serializer.data["return_date"][:10]

        return Response(return_data, status=status.HTTP_201_CREATED, headers=headers)


class LoanDetailView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsColaborator]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get_queryset(self):
        username = self.request.user
        user = get_object_or_404(User, username=username)
        if user.is_superuser:
            queryset = super().get_queryset()
            return queryset
        else:
            queryset = super().get_queryset()
            return queryset.filter(user=self.request.user)
