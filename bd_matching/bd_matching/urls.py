"""
URL configuration for bd_matching project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from matching_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("template_sample/", views.template_sample.as_view(), name="template_sample"),
    path("form_sample/", views.form_sample.as_view(), name="form_sample"),
    path("model_sample/", views.model_sample.as_view(), name="model_sample"),
    path("main/",views.main.as_view(), name = "main"),
    path("choice/",views.choice.as_view(), name = "choice")
]
