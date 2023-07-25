from rest_framework import permissions
from .models import User
from rest_framework.views import View


class IsCollaborator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user.is_superuser
        return True


class IsCollaboratorOrStudent(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        if request.method == "POST" and request.data.get("user_status") == "collaborator":
            return request.user.is_superuser
        return True
