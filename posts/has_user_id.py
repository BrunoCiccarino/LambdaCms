from rest_framework.permissions import BasePermission

class HasUserId(BasePermission):
    def has_permission(self, request, view=None):
        if request.method == 'POST':
            return request.data.get('user_id') is not None
        return True
