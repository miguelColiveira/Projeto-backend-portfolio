from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView
from copies.models import Copy
from copies.serializer import CopySerializer


from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsCollaborator


class CopyView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]

    queryset = Copy
    serializer_class = CopySerializer


class CopyDetailView(RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]

    queryset = Copy
    serializer_class = CopySerializer
