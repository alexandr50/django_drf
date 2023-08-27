from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проврка прав на собственность"""
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsModerator(BasePermission):
    """Проверка прав модератора"""

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(
            name="модератор",
        ).exists() and request.method in ["GET", "PUT", "PATCH"]
