from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView)
from .models import Home

class Index(ListView):
    template_name = 'home/index.html'
    context_object_name = 'imagenesPortada'
    model=Home







