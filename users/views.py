from crm.views import BaseView
from .models import User
from .serializers import UserSerializer, UserDetailSerializer
from .tasks import add
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin


# Create your views here.

class UserDetail(BaseView):

    def get(self, request, *args, **kwargs):
        pk = int(kwargs['pk'])
        import pdb; pdb.set_trace()
        instance = UserDetailSerializer(instance=User.objects.get(pk=pk), context={'request': request})
        return instance

class UserList(BaseView):
    def get(self, request, *args, **kwargs):
        instance = UserSerializer(instance=User.objects.all(), context={'request': request}, many=True)
        return instance


class RequestTracker(LoggingMixin, generics.GenericAPIView):
    def get(self, request):
        return Response('with logging')
