from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Pagination(object):

    def __init__(self, request, items, meta, page_size=20):
        self.items = items
        self.meta = meta
        self.page_size = int(request.GET.get('page_size', page_size))
        self.page_no = int(request.GET.get('page', 1))
        self.url = request.path
        self.response = {}
        self.paginator = None
        self.status_code = 200

    def get_next_link(self):
        try:
            if self.paginator.page(self.page_no).has_next():
                return self.url + '?page=' + str(self.paginator.page(self.page_no).next_page_number())
        except EmptyPage:
            pass
        except PageNotAnInteger:
            pass
        return None

    def get_previous_link(self):
        try:
            if self.paginator.page(self.page_no).has_previous():
                return self.url + '?page=' + str(self.paginator.page(self.page_no).previous_page_number())
        except EmptyPage:
            pass
        except PageNotAnInteger:
            pass
        return None

    @property
    def start_index(self):
        return self.paginator.page(self.page_no).start_index()

    @property
    def end_index(self):
        return self.paginator.page(self.page_no).end_index()

    def paginate(self):
        self.paginator = Paginator(self.items, per_page=self.page_size)
        try:
            obj_list = self.paginator.page(self.page_no).object_list

        except PageNotAnInteger:
            self.response = {"err_message": "Bad url"}
            self.status_code = 400
            return

        except EmptyPage:
            self.page_no = 1
            obj_list = self.paginator.page(self.page_no).object_list

        self.meta = {
            "page_no": self.page_no,
            "type": "list",
            "total_items": len(obj_list),
            "next_page": self.get_next_link(),
            "previous_page": self.get_previous_link(),
            # "start_index": self.start_index,
            # "end_index": self.end_index,
        }

        self.response = {
            "items": obj_list,
            "meta": self.meta
        }

    def paginated_response(self):
        self.paginate()
        return self.response
