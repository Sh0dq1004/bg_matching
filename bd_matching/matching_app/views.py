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

class admin_huriwake(TemplateView):
    template_name = "admin_huriwake.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["var"] = "admin_hurikwake"
        return context
    
class main(TemplateView):
    template_name = "main.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["var"] = "main"
        return context

class choice(TemplateView):
    template_name = "choice.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["var"] = "choice"
        return context
    
class main(TemplateView):
    template_name = "main.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["var"] = "main"
        return context

class choice_detail(TemplateView):
    template_name = "choice_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["var"] = "choice_detail"
        return context

class wait(TemplateView):
    template_name = "wait.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["var"] = "wait"
        return context

class result(TemplateView):
    template_name = "result.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["var"] = "result"
        return context