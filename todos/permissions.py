from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (obj.owner == request.user) or (request.user and request.user.is_staff)
