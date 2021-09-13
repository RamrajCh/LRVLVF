from django.contrib import admin

from .models import Controller, ElectricalParameters

# Register your models here.

@admin.register(Controller)
class ControllerAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    list_filter = ('name', 'created', 'updated')
    search_fields = ('name',)


@admin.register(ElectricalParameters)
class ElectricalParametersAdmin(admin.ModelAdmin):
    list_display = ('controller', 'rms_voltage', 'rms_current', 'active_power', 'reactive_power', 'phase_connection', 'updated')
    list_filter = ('controller',)
    search_fields = ('controller',)