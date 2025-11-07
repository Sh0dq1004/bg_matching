from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Person
from .form import User
from django.http import HttpResponse
from . import bd_maker


# Create your views here.
class template_sample(TemplateView):
    template_name = "template_sample.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["var"] = "template_sample"
        return context

class form_sample(CreateView):
    template_name = "create_sample.html"
    model = User
    fields = ("name", "table_num", "favorite")
    success_url = "/model_sample/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["var"] = "create_sample"
        return context


class model_sample(TemplateView):
    template_name="model_sample.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["var"] = "create_sample"
        context["data"] = BoardGame.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        if 'datamaker' in request.POST:
            print("Data Maker button pressed!")
            # 実際の処理をここに書く
            bd_maker.main()
        return super().get(request, *args, **kwargs)

class main(CreateView):
    template_name = "main.html"
    model = Person
    fields = ("name", "table_num", "favorite")
    success_url = "/choice/"

    def post(self, request, *args, **kwargs):
        if 'datamaker' in request.POST:
            print("Data Maker button pressed!")
            # 実際の処理をここに書く
            bd_maker.main()
        return super().get(request, *args, **kwargs)

class choice(CreateView):
    template_name = "choice.html"
    model = User
    fields = ("name", "table_num", "favorite")
    success_url = "/choice/"

    def post(self, request, *args, **kwargs):
        if 'datamaker' in request.POST:
            print("Data Maker button pressed!")
            # 実際の処理をここに書く
            bd_maker.main()
        return super().get(request, *args, **kwargs)

class wait(CreateView):
    template_name = "wait.html"
    model = User
    fields = ("name", "table_num", "favorite")
    success_url = "/wait/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["var"] = "/wait/"
        return context

