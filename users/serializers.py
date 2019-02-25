from rest_framework import serializers
from .models import User
from permissions.serializers import PermissionSerializer
import urlparse


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

    @classmethod
    def construct_url(cls, url):
        return urlparse.urlsplit(url).path

    def to_representation(self, instance):
        ret = super(UserSerializer, self).to_representation(instance)
        user_url = self.construct_url(ret.get('url'))
        ret.update({'url': user_url})
        permission_url = self.construct_url(ret.get('permission'))
        ret.update({'permission': permission_url})
        return ret


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    permission = PermissionSerializer(required=True)

    class Meta:
        model = User
        exclude = ['password']

    @classmethod
    def construct_url(cls, url):
        return urlparse.urlsplit(url).path

    def to_representation(self, instance):
        ret = super(UserDetailSerializer, self).to_representation(instance)
        url = self.construct_url(ret.get('url'))
        ret.update({'url': url})
        return ret
