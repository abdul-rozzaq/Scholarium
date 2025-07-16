from rest_framework.permissions import BasePermission


class TenantUserPermission(BasePermission):
    """
    Faqat:
    - superuser yoki staff bo'lsa
    - yoki user o'ziga tegishli school ichida bo'lsa ruxsat beriladi
    """

    def has_permission(self, request, view):

        user = request.user
        tenant = getattr(request, "tenant", None)

        if not user or not user.is_authenticated:
            return False

        if user.is_staff or user.is_superuser:
            return True

        if tenant and user.school and tenant == user.school:
            return True

        return False
