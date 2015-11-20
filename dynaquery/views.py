import functools
import json
import operator

from django.db.models import Q
from django.http import HttpResponse

from .models import Car


def _make_lookup(data):
    q_filter = [
        Q(color=item['color'],
          model=item['model'],
          year=item['year'],
          cc=item['cc'])
        for item in data
    ]

    if q_filter:
        return functools.reduce(operator.or_, q_filter)

    return q_filter


def index(request):
    data = json.loads(request.body.decode())

    q_filter = _make_lookup(data)
    qs = Car.objects.filter(q_filter).exists()

    if qs:
        qs = Car.objects.filter(q_filter)
        qs.update(checked=True)

        return HttpResponse("Data updated")

    return HttpResponse("No data updated")
