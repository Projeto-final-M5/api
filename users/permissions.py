from rest_framework import permissions

class IsAdmOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj or request.user.is_superuser