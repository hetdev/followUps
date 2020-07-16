from django.db import models
from django.utils.translation import ugettext_lazy as _


class Client(models.Model):
    business_name = models.CharField(max_length=200, blank=False, null=False)
    public_name = models.CharField(max_length=200, blank=True, null=True)
    nit = models.CharField(max_length=200, blank=False, null=False)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=False, null=False)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    contact_name = models.CharField(max_length=200, blank=False, null=False)
    position = models.CharField(max_length=200, blank=True, null=True)
    billing_email = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(_('email address'), blank=False, null=False, unique=False)

    def __str__(self):
        return self.business_name
