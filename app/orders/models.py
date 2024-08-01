from django.db import models
from bikes.models import Bike
from accounts.models import Account
import time

class Order(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Account, on_delete=models.CASCADE)

    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(blank=True, null=True)

    worth = models.DecimalField(max_digits=10, default=0, decimal_places=1)

    def worth_calculation(self):
        timediff = self.finished_at - self.started_at
        cost_per_second = self.bike.price / 3600
        self.worth = round(timediff.seconds * cost_per_second, 2)

    def save(self, *args, **kwargs):
        if self.finished_at:
            self.worth_calculation()
        super().save(*args, **kwargs)
