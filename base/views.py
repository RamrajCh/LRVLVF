from django.shortcuts import render

from controller.models import ElectricalParameters as E, Controller as C

# Create your views here.

def home_page(request):
    controller = C.objects.all()
    parameters = []
    for p in controller:
        if E.objects.filter(controller=p).exists():
            parameters.append(E.objects.filter(controller=p).order_by('-created')[0])
    
    return render(request,
                'base/home.html',
                {'parameters': parameters,})