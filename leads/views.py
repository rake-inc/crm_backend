from django.views import View
from crm.views import BaseView
from .models import Lead, Comment, Reminders


# Create your views here.

class LeadsView(BaseView):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        data = request.data['items']
        Lead.objects.create(**data)
        return self.json_response(data)

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, reques, *args, **kwargs):
        pass


class CommentsView(BaseView):

    def get(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        data = request.data['items']
        Comment.objects.create(**data)
        return self.json_response(data)

    def delete(self, request, *args, **kwargs):
        pass


class RemindersView(BaseView):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        data = request.data['items']
        Reminders.objects.create(**data)
        return self.json_response(data)

    def put(self, request, *args, **kwargs):
        data = request.data['items']
        Reminders.objects.update(**data)
        return self.json_response({})

    def delete(self, request, *args, **kwargs):
        pass
