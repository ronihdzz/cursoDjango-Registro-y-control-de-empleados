from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from  .forms import NewDepartamentoForm

from .models import Departamento
from applications.persona.models import Empleado, Habilidades
from django.urls import reverse_lazy

class DepartamentoListView(ListView):
    model=Departamento
    template_name = 'departamento/listaDepartamentos.html'
    context_object_name = 'datos'


# Create your views here.
class NewDepartamento(FormView):
    template_name = 'departamento/newDepartamento.html'
    form_class = NewDepartamentoForm
    success_url = reverse_lazy('departamento_app:departamento_lista')

    def form_valid(self, form):
        print("***ESTAMOS EN EL FORM VALID")
        nombre=form.cleaned_data['nombre']
        apellido=form.cleaned_data['apellidos']
        departamento=form.cleaned_data['departamento']
        shorname=form.cleaned_data['shorname']
        avatar=form.cleaned_data['avatar']
        habilidades=form.cleaned_data['habilidades']

        print("HABILIDADES",habilidades)

        depa=Departamento(
            name=departamento,
            shor_name=shorname,
        )
        depa.save()

        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1', # Administrador
            departamento=depa,
            avatar=avatar,
        ).habilidades.set(habilidades)

        return super(NewDepartamento,self).form_valid(form)


