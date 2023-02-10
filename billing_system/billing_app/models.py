from django.db import models
from django.contrib.auth.models import User


class Bill(models.Model):
    buyer = models.ForeignKey(User, related_name='buyer_bills', on_delete=models.CASCADE)
    vendor = models.ForeignKey(User, related_name='vendor_name', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.product
