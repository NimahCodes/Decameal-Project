from rest_framework import permissions


class IsKitchenStaffOrReadOnly(permissions.BasePermission):
    # Meal upload permissions are only allowed for kitchen staff users. Allow all users to read.
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == "Kitchen Staff"
