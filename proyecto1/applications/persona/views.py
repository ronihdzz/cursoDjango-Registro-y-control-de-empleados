from django.views.generic import (ListView,DetailView,CreateView,
                                  TemplateView,UpdateView,DeleteView)
from .models import Empleado

from django.urls import reverse_lazy

class VerTodosEmpleados_listView(ListView):
    '''
    Mostrar una lista con todos los empleados
    '''

    template_name ='persona/todosEmpleados.html'
    model = Empleado
    context_object_name = 'datos'
    paginate_by = 10

    def get_queryset(self):
        '''
        Si se sobreescribe este metodo ya no sera necesario indicarle
        un modelo a la clase, ya que este metodo es el que decide
        que información regresar
        '''

        palabraClave=self.request.GET.get('kword','')
        lista= Empleado.objects.filter(
            first_name__icontains=palabraClave
        )
        return lista


class DetalleEmpleado_detailView(DetailView):
    template_name ='persona/detalleEmpleado.html'
    model = Empleado


class AdministrarEmpleados_listView(ListView):
    model = Empleado
    template_name = 'persona/administracionEmpleados.html'
    context_object_name = 'datos'
    paginate_by = 10

class EditarEmpleado(UpdateView):
    template_name = 'persona/editarEmpleado.html'
    model = Empleado
    fields = ('__all__')
    success_url = reverse_lazy('persona_app:persona-administrarEmpleados')


class EliminarEmpleado(DeleteView):
    template_name = 'persona/eliminarEmpleado.html'
    model = Empleado
    success_url = reverse_lazy('persona_app:persona-administrarEmpleados')
    context_object_name = 'empleadoEliminar'


class EmpleadosPorArea_listView(ListView):
    template_name ='persona/empleadosPorArea.html'
    model = Empleado
    context_object_name = 'datos'
    def get_queryset(self):
        '''
        Retornara el resultado de un filtro de busqueda
        :return:
        siempre debe retornar una lista
        '''

        area=self.kwargs['area']
        lista= Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista


class AddEmpleado(CreateView):
    template_name = 'persona/addPersona.html'
    model = Empleado
    fields = ('__all__')
    # significa que se rederigira a la misma pagina
    success_url = reverse_lazy('persona_app:persona-administrarEmpleados')


class BusquedaPerfiles(ListView):
    template_name = 'persona/busquedaPerfiles.html'
    context_object_name = 'datos'
    model = Empleado
    paginate_by = 3
    ordering = 'first_name'

    def get_queryset(self):
        perfil=self.request.GET.get('nombre_perfil_x','')
        lista= Empleado.objects.filter(
            departamento__shor_name=perfil
        )
        if len(lista)<1:
            lista=['Sin resultados']
        return lista










