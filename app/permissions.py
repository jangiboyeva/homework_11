from rest_framework.permissions import BasePermission,SAFE_METHODS
from .models import User

class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS :
            return True
        
        return obj.from_user == request.user