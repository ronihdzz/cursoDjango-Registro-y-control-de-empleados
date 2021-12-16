
from django.urls import path
from applications.departamento import views


app_name='departamento_app'

urlpatterns = [
    path('newDepartamento/',
         views.NewDepartamento.as_view(),
         name='newDepartamento'),

    path('departamento_lista/',
    views.DepartamentoListView.as_view(),
    name='departamento_lista')
]










