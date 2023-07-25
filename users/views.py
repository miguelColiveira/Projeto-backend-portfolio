from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from users.permissions import IsCollaborator, IsCollaboratorOrStudent
from users.serializers import UserSerializer


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaboratorOrStudent]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_destroy(self, instance: User):
        instance.is_active = False
        instance.save()
