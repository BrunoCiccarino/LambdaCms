from rest_framework.permissions import BasePermission

class IsPostOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allows access if the user making the request is the owner of the post
        return obj.user_id == request.data.get('user_id')