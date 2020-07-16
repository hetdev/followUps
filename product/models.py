from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProductAdministrator(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(_('email address'), blank=False, null=False, unique=False)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=400, blank=False, null=False)
    quantity = models.SmallIntegerField(blank=False, null=False)
    tariff = models.SmallIntegerField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    value = models.DecimalField(max_digits=23, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.name
