from django.db import models

from product.models import ProductAdministrator, Product


class Order(models.Model):
    city = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=False, null=False)
    activation_date = models.DateField(blank=False, null=False)
    observations = models.CharField(max_length=400, blank=True, null=True)
    project = models.CharField(max_length=200, blank=False, null=False)
    months = models.SmallIntegerField(blank=False, null=False)
    sub_total = models.DecimalField(max_digits=23, decimal_places=2, blank=False, null=False)
    vat = models.DecimalField(max_digits=23, decimal_places=2, blank=False, null=False)
    total = models.DecimalField(max_digits=23, decimal_places=2, blank=False, null=False)
    commercial_code = models.CharField(max_length=200, blank=True, null=True)

    product_administrator = models.ForeignKey(
        ProductAdministrator,
        null=True,
        blank=True,
        related_name='order_product_administrator',
        on_delete=models.CASCADE)

    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.project
