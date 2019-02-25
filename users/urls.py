from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'auth/(?P<pk>\d+)/$',views.UserDetail.as_view(), {'type':'detail'}, name='user-detail'),
        url(r'auth/$',views.UserList.as_view(),{}, name='no-list'),
]
