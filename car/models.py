from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=255, blank=False)
    brand = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    color = models.CharField(max_length=255, blank=False)
    year = models.DateField(blank=False)
    price = models.PositiveBigIntegerField(blank=False)

    def __str__(self):
        return f'{self.brand} {self.model}'
