from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """this permission is only for owner of a profile"""
    def has_object_permission(self, request, view, obj):
        """check if user is owner of profile"""

        if request.method in permissions.SAFE_METHODS:
            """handles to get user profile details"""

            return True

        return obj.id == request.user.id


class PostOwnProfile(permissions.BasePermission):
    """this permission is only for owner of a profile"""

    def has_object_permission(self, request, view, obj):
        """check if user is owner of profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
