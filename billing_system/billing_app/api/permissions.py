from rest_framework import permissions
from billing_app.models import Bill
        
        
class IsStaffUser(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
    

    
class IsBuyer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.buyer == request.user) 


class IsVendorOrBuyer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.vendor == request.user or obj.buyer == request.user) 