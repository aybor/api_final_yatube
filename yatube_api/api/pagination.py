from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.LimitOffsetPagination):
    def get_paginated_response(self, data):
        if self.offset or self.limit:
            return Response(OrderedDict([
                ('count', self.count),
                ('next', self.get_next_link()),
                ('previous', self.get_previous_link()),
                ('results', data)
            ]))
        return Response(data)
