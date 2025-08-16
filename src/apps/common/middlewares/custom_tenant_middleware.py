from django_tenants.middleware import TenantMainMiddleware
from django_tenants.utils import remove_www

from apps.common.utils import remove_api


class CustomTenantMiddleware(TenantMainMiddleware):

    @staticmethod
    def hostname_from_request(request):
        hostname = remove_www(request.get_host().split(":")[0])

        return remove_api(hostname)
