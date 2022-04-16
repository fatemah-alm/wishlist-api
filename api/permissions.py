from rest_framework import permissions

class UserCanOnlyRead(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.method)
        if (request.method in permissions.SAFE_METHODS):
            return True

        return bool(request.user and request.user.is_staff)
        
    
class VipCanOnlyView(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if (request.user.is_staff or request.user.id == obj.added_by.id):
            return True
        return False
        

      
            
        
        
    
        
        
            