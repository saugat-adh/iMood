from rest_framework import permissions

class IsUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if obj.created_by == request.user:
            return True
        else:
            return False