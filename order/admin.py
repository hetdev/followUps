from django.contrib import admin
from import_export.admin import ExportActionMixin

from order.models import Order


class OrderAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'project',
        'total',
        'date',
        'activation_date'
    )


admin.site.register(Order, OrderAdmin)
