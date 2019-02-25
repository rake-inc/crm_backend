import json
from django.utils.deprecation import MiddlewareMixin


class CustomMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.method in ['POST', 'PUT', ] and request.META.get('CONTENT_TYPE', "") == 'application/json':
            try:
                json.loads(request.body)
            except ValueError:
                from django.http import JsonResponse
                return JsonResponse({"error_message": "Improper Content-Type"}, status=400)

    def process_response(self, request, response):
        # import pdb;pdb.set_trace()
        # from crm import settings
        # if response.status_code == 404 and not settings.DEBUG:
        #     from django.http import JsonResponse
        #     return JsonResponse({"error_message":"url not found"}, status=response.status_code)
        return response