from rest_framework.permissions import BasePermission


class IsGroupOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsNotificationTemplateOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.group.owner == request.user
