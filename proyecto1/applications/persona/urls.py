from django.contrib import admin
from django.urls import path
from applications.persona import views

app_name='persona_app'

urlpatterns = [
    #path('',
    #     views.Inicio.as_view(),
    #     name='inicio'
    #),
    path( 'persona/verTodosEmpleados/',
          views. VerTodosEmpleados_listView.as_view(),
          name='persona-verTodosEmpleados'), 
    path('persona/verDetalleEmpleado/<pk>',
         views.DetalleEmpleado_detailView.as_view(),
         name='persona-verDetalleEmpleado'),

    path('persona/administrarEmpleados/',
         views.AdministrarEmpleados_listView.as_view(),
         name='persona-administrarEmpleados'
         ),

    path('editarEmpleado/<pk>',
         views.EditarEmpleado.as_view(),
         name='editarEmpleado'
         ),

    path('eliminarEmpleado/<pk>',
         views.EliminarEmpleado.as_view(),
         name='eliminarEmpleado'
         ),

    path('empleadosPorArea/<area>/',
         views.EmpleadosPorArea_listView.as_view(),
         name='empleadosPorArea'
         ),


    path('addEmpleado/',
         views.AddEmpleado.as_view(),
         name='addEmpleado'),


]

