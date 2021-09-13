from django.shortcuts import render
from django.views.generic import TemplateView

from controller.models import ElectricalParameters

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'base/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parameters'] = ElectricalParameters.objects.all()
        return context