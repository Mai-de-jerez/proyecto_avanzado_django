from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "core/home.html"
    
    
    def get(self, request, *args, **kwargs):
        # Aquí puedes realizar cualquier lógica adicional antes de renderizar la plantilla
        return render(request, self.template_name, {"title": "Mi super web Playground"})
        

class SamplePageView(TemplateView):
    template_name = "core/sample.html"
