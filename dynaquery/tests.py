import json
import random

from django.test import TestCase
from django.core.urlresolvers import reverse

from .factories import CarFactory


class CarBaseTest(TestCase):

    def setUp(self):
        car_list = [CarFactory() for _ in range(1, random.randint(5, 100))]
        self.index_url = reverse('index')
        self.payload = [
            {'color': car.color,
             'cc': car.cc,
             'year': car.year,
             'model': car.model}
            for car in car_list
        ]

    def test_max_3_queries(self):
        with self.settings(DEBUG=True):
            from django.db import connection

            self.assertEqual(len(connection.queries), 0)

            request = self.client.post(self.index_url,
                                       data=json.dumps(self.payload),
                                       content_type='application/json')

            self.assertEqual(len(connection.queries), 3)
