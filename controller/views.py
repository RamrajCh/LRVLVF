from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods
from .models import Controller, ElectricalParameters

# Create your views here.

def add_to_database(request, controller_id):
    controller = get_object_or_404(Controller, id=controller_id)
    rms_voltage = request.GET.get('v', '')
    rms_current = request.GET.get('i', '')
    active_power = request.GET.get('p', '')
    reactive_power = request.GET.get('q', '')
    phase_connection = request.GET.get('abc', '')
    if all([rms_voltage, rms_current, active_power, reactive_power]):
        try:
            parameter = ElectricalParameters(
                controller=controller,
                rms_voltage=float(rms_voltage), 
                rms_current=float(rms_current), 
                active_power=float(active_power),
                reactive_power=float(reactive_power),
                phase_connection=phase_connection,
                )
            parameter.save()
        except Exception:
            parameter = ElectricalParameters.objects.filter(controller=controller).first()
            parameter.rms_voltage = float(rms_voltage)
            parameter.rms_current = float(rms_current)
            parameter.active_power = float(active_power)
            parameter.reactive_power = float(reactive_power)
            parameter.phase_connection = phase_connection
            parameter.save()
        messages.success(request, f"{controller}'s parameter updated!")
    else:
        messages.error(request, "Parameter update failed!")
    return redirect('base:home')
