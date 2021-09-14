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
        parameter = ElectricalParameters(
                controller=controller,
                rms_voltage=float(rms_voltage), 
                rms_current=float(rms_current), 
                active_power=float(active_power),
                reactive_power=float(reactive_power),
                phase_connection=phase_connection,
                )
        parameter.save()
        messages.success(request, f"{controller}'s parameter updated!")
    else:
        messages.error(request, "Parameter update failed!")
    return redirect('base:home')


def view_controller_detail(request, controller_id):
    controller = get_object_or_404(Controller, id=controller_id)
    parameters = ElectricalParameters.objects.filter(controller=controller)[:10]
    master = False
    if controller_id == 1:
        master = True

    return render(request,
                'controller/detail.html',
                {'controller': controller,
                'parameters': parameters,
                'master': master})