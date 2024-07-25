# utilities/permissions.py
from rest_framework.permissions import BasePermission

class AllowAnyWithToken(BasePermission):
    def has_permission(self, request, view):
        return True
