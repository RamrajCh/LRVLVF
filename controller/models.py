from django.db import models
from django.db.models.fields import DecimalField

# Create your models here.

class Controller(models.Model):
    name = models.CharField(db_index=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
    
    def __str__(self) -> str:
        return f'Controller: {self.name}'


class ElectricalParameters(models.Model):
    rms_voltage = models.DecimalField(max_digits=10, decimal_places=5)
    rms_current = models.DecimalField(max_digits=10, decimal_places=5)
    active_power = models.DecimalField(max_digits=10, decimal_places=5)
    reactive_power = models.DecimalField(max_digits=10, decimal_places=5)
    phase_connection = models.CharField(max_length=1, blank=True)
    controller = models.OneToOneField(Controller, on_delete=models.CASCADE, related_name='parameters')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('controller',)
    
    def __str__(self) -> str:
        return f'Parameters for Controller: {self.controller.name}'