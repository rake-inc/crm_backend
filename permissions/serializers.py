from rest_framework import serializers
from .models import Permission
import urlparse


class PermissionSerializer(serializers.HyperlinkedModelSerializer):

    url_field_name = 'resource_url'

    class Meta:
        model = Permission
        fields = '__all__'

    @classmethod
    def construct_url(cls, url):
        return urlparse.urlsplit(url).path

    def to_representation(self, instance):
        ret = super(PermissionSerializer, self).to_representation(instance)
        url = self.construct_url(ret.get(self.url_field_name))
        ret.update({self.url_field_name: url})
        return ret
