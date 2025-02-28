from django.db import models


class Bike(models.Model):
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    rent_is = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model
