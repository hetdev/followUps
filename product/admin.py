from django.contrib import admin
from product.models import ProductAdministrator, Product


class ProductAdministratorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email'
    )


admin.site.register(ProductAdministrator, ProductAdministratorAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'quantity',
        'value'
    )


admin.site.register(Product, ProductAdmin)
