from django.contrib import admin
from client.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'business_name'
    )


admin.site.register(Client, ClientAdmin)
