from rest_framework import permissions
from django.http import HttpRequest

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permissions that allow owners of an object to edit it.
    Assumes the model instance has `owner` attr."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user
    
    def has_permission(sel, request: HttpRequest, view) -> bool:
        """
        Checks if user has permission to perform the requested action.
        Params:
            request: Initiated incoming request.
            view: View being accessed.
        Returns:
            bool: True if request is safe or if user = admin, Else: False"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user and request.user.is_staff