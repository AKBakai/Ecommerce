from django.db import models
from wear.models import Wear
from django.contrib.auth.models import User

class Cart(models.Model):
    wear = models.ForeignKey(Wear, on_delete=models.CASCADE, related_name='cart_wear')
    amount = models.PositiveIntegerField(null=True, blank=True)
    price = models.ForeignKey(Wear, on_delete=models.CASCADE)
    full_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.full_price = self.wear.price * self.amount
        super(Cart, self).save(*args, **kwargs)

