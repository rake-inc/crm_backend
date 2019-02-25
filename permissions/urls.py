from django.conf.urls import url
from .views import *

urlpatterns = [
        url(r'permissions/(?P<pk>[a-z0-9-]{36})/$',PermisionDetail.as_view(),{'type':'detail'},name='permission-detail'),
        url(r'permissions/$', PermissionList.as_view(), name='permission-list'),
]
