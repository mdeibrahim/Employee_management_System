from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any authenticated request,
        # so we'll always allow GET, HEAD or OPTIONS requests.


        if request.method in permissions.SAFE_METHODS: # SAFE_METHODS are GET, HEAD, OPTIONS
            return obj.user == request.user # so even for SAFE_METHODS, we check ownership.

        # Write permissions are only allowed to the owner of the employer.
        return obj.user == request.user

class IsAuthenticatedAndOwner(permissions.BasePermission):
    """
    Custom permission:
    - Ensures the user is authenticated.
    - For object-level permissions (retrieve, update, delete), ensures the user is the owner.
    - For list/create, authentication is sufficient (filtering for list is done in queryset).
    """
    def has_permission(self, request, view):
        # Allow access if user is authenticated.        
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        
        # This applies to retrieve (GET /employers/<id>/), update (PUT), and delete (DELETE).
        if not request.user or not request.user.is_authenticated:
            return False
        return obj.user == request.user

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the employer
        return obj.user == request.user

