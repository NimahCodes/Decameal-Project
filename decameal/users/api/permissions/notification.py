from rest_framework import permissions


class IsNotificationOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        # Notifications are to be viewed only by owners
        return request.user.is_authenticated and view.kwargs["pk"] == request.user.id


class Notifications(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return (
                request.user.is_authenticated and view.kwargs["pk"] == request.user.id
            )
        if request.method == "POST":
            return (
                request.user.is_authenticated and request.user.role == "Kitchen Staff"
            )
        return request.user.is_authenticated
