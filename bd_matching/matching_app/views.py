from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

# Create your views here.
class template_sample(TemplateView):
    template_name = "template_sample.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["var"] = "template_sample"
        return context

class form_sample(TemplateView):
    template_name = "create_sample.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["var"] = "create_sample"
        return context
