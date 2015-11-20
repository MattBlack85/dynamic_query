import datetime

import factory
import factory.fuzzy as fuzzy

from .models import Car, MODEL_CHOICES, COLOR_CHOICES


class CarFactory(factory.django.DjangoModelFactory):
    color = fuzzy.FuzzyChoice([color[0] for color in COLOR_CHOICES])
    model = fuzzy.FuzzyChoice([model[0] for model in MODEL_CHOICES])
    year = fuzzy.FuzzyInteger(2000, 2015)
    cc = fuzzy.FuzzyInteger(1000, 2500, 100)

    class Meta:
        model = Car
