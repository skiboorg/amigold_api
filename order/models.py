
from django.db import models


class Order(models.Model):
    sessionID = models.CharField(max_length=255, blank=True, null=True)
    totalPrice = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)

class OrderItem(models.Model):
    cart = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, related_name='products')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, blank=True, null=True)
    productPrice = models.ForeignKey('product.ProductPrice', on_delete=models.CASCADE, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    totalPrice = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)




