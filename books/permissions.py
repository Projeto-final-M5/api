from rest_framework import permissions

class IsAdmOrOwnerBook(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
      
      return request.user.id == obj.user_id or request.user.is_superuser

