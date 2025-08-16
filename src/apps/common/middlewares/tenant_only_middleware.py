from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse


class TenantOnlyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        schema_name = request.tenant.schema_name

        if schema_name == "public" and request.path.startswith("/api/"):
            return JsonResponse({"detail": "Bu endpoint faqat tenantlar uchun mo'ljallangan."}, status=403)

        return self.get_response(request)
