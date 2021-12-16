from django.db import models

# Create your models here.
class Departamento(models.Model):
    # El primer parametro es el texto que aparecera en el administrador de django
    name=models.CharField('Nombre',max_length=50)
    shor_name=models.CharField('Nombre corto',max_length=20)

    #valor por defecto es igual a False
    anulate=models.BooleanField('Anulado',default=False)

    def __str__(self):
        return '{} - {} - {}'.format(self.id,self.name,self.shor_name)


