from rest_framework import permissions


class IsDecadevOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        #  update permissions are only allowed for subscribers
        return request.user.is_authenticated and request.user.role != "Kitchen Staff"
