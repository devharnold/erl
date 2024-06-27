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

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to allow owners of an object to edit it
    Assuming the model instance has an `owner` attribute
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user
    
    def has_permission(self, request: HttpRequest, view) -> bool:
        """Checks if user has permission to perform the requested action
        Params:
            request: Initiated incoming request
            view: view being accessed
        Returns:
            bool: True if request is safe or if user is authenticated, else False
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user and request.user.is_authenticated
    
class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """Custom permission to allow authenticated users to edit, read-only for others"""
    def has_permission(self, request: HttpRequest, view) -> bool:
        """
        Checks if user has permission to perform the requested action
        Params:
            request: Initiated incoming request
            view: the view being accessed
        Returns:
            bool: True if request is safe or if user is authenticated, else False
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user and request.user.is_authenticated
