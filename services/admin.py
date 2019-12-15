from django.contrib import admin
from .models import Service


class serviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'port']
admin.site.register(Service, serviceAdmin)
