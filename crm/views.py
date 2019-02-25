from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from crm.pagination import Pagination
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response 

class BaseView(APIView):
    response_context = {
        "meta": {},
        "items": []
    }
    authentication_classes = []
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        import pdb;pdb.set_trace()
        # if request.method in ['POST', 'PUT'] and request.META.get('CONTENT_TYPE', 'text/plain') == 'application/json':
        #     setattr(request, 'data', json.loads(request.body))
        if kwargs.get('type',False) == 'detail':
            setattr(request, 'paginate', False)
        else:
            setattr(request, 'paginate', True)
        response = super(BaseView, self).dispatch(request, *args, **kwargs)
        return self.json_response(response)

    def json_response(self, items, meta=response_context['meta'], status_code=200, **kwargs):
        if isinstance(items, (JsonResponse, HttpResponse, Response)):
            return items

        if self.request.paginate:
            pagination = Pagination(self.request, items, meta)
            return JsonResponse(pagination.paginated_response(), status=pagination.status_code)
        else:
            meta.update({"type":"detail"})
            self.response_context = {
                "items": items,
                "meta": meta,
            }
            return JsonResponse(self.response_context, status=status_code)

    def http_response(self, content, status_code=200):
        raise NotImplementedError("Method defined but not yet implemented. Please go to BaseView to implement it")
