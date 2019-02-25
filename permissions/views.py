from django.shortcuts import render
from crm.views import BaseView
from .serializers import PermissionSerializer
from .models import Permission
# Create your views here.
    
class PermisionDetail(BaseView):

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        instance = PermissionSerializer(instance=Permission.objects.get(pk=pk), context={'request':request})
        return self.json_response(instance.data)

class PermissionList(BaseView):

    def get(self, request, *args, **kwargs):
        instance = PermissionSerializer(instance=Permission.objects.all(), context={'request':request}, many=True)
        return self.json_response(instance.data)
