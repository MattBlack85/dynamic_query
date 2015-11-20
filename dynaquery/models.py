import uuid

from django.db import models

COLOR_CHOICES = (
    (1, 'white'),
    (2, 'black'),
    (3, 'grey'),
    (4, 'red'),
)

MODEL_CHOICES = (
    (1, 'kia'),
    (2, 'subaru'),
    (3, 'audi'),
    (4, 'alfa romeo')
)


class Car(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    color = models.CharField(max_length=15, choices=COLOR_CHOICES)
    year = models.PositiveSmallIntegerField()
    model = models.CharField(max_length=15, choices=MODEL_CHOICES)
    cc = models.PositiveSmallIntegerField()
    checked = models.BooleanField(default=False)
