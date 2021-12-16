from django.contrib import admin
from .models import Empleado,Habilidades
# Register your models here.

class FormatoTablaHabilidades(admin.ModelAdmin):
    list_display = (
        'id',
        'habilidad',
    )
class FormatoTablaEmpleados(admin.ModelAdmin):
    list_display = (
        'id',
        'nombreCompleto',
        #'first_name',
        #'last_name',
        'job',
        'departamento',
    )
    search_fields = ('first_name','last_name',)
    list_filter = ('departamento','habilidades')

    def nombreCompleto(self,objt):
        return '{} {}'.format(objt.first_name,objt.last_name)

admin.site.register(Habilidades,FormatoTablaHabilidades)
admin.site.register(Empleado,FormatoTablaEmpleados)



