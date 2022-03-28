from rest_framework import permissions


class IsKitchenStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        # Ticket upload permissions are only allowed for kitchen staff
        return request.user.is_authenticated and request.user.role == "Kitchen Staff"
